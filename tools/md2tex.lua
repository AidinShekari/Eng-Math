-- md2tex.lua — pandoc Lua filter: course Markdown → semantic LaTeX.
--
--   ## Heading            →  \EMsection{title}{plain title}
--   ### Heading           →  \EMsubsection{title}{plain title}
--   $x$  /  $$x$$         →  \EMim{x}  /  \[ x \]
--   ::: {.definition title="…"} … :::   (also theorem, important, example,
--                           exercise, remark, proof, solution)
--   ```{.figure #name caption="…"}      →  \EMfigure{name}{caption}
--
-- Environment variables: EM_LANG (fa|en), EM_FIGDIR (template/figures).

local LANG = os.getenv("EM_LANG") or "en"
local RTL = LANG == "fa"
local FIGDIR = os.getenv("EM_FIGDIR") or "template/figures"

local ENVS = {
  definition = "EMdefinition", theorem = "EMtheorem", important = "EMimportant",
  example = "EMexample", exercise = "EMexercise", remark = "EMremark",
  proof = "EMproof", lemma = "EMlemma", proposition = "EMproposition",
  corollary = "EMcorollary",
}
local OPEN_ENVS = { solution = "EMsolution" }

---------------------------------------------------------------------------
-- helpers
---------------------------------------------------------------------------
local function raw(s) return pandoc.RawInline("latex", s) end
local function rawb(s) return pandoc.RawBlock("latex", s) end

local function has_arabic(s)
  for _, cp in utf8.codes(s) do
    if (cp >= 0x0600 and cp <= 0x06FF) or (cp >= 0x0750 and cp <= 0x077F)
       or (cp >= 0xFB50 and cp <= 0xFDFF) or (cp >= 0xFE70 and cp <= 0xFEFF) then
      return true
    end
  end
  return false
end

local function has_latin(s) return s:find("%a") ~= nil end

-- the text of a balanced {...} group starting at position i (s:sub(i,i) == "{")
local function balanced(s, i)
  local depth = 0
  for j = i, #s do
    local c = s:sub(j, j)
    if c == "{" then depth = depth + 1
    elseif c == "}" then
      depth = depth - 1
      if depth == 0 then return s:sub(i + 1, j - 1), j end
    end
  end
  return nil, nil
end

-- mathematics ---------------------------------------------------------------
local function fix_math(s)
  s = s:gsub("\\checkmark", "\\EMcheck ")
  -- a row gap "\\[7mm]" is ignored by amsmath once unicode-math and bidi are loaded; inside
  -- cases it is written as an explicit skip instead
  s = s:gsub("\\begin{cases}(.-)\\end{cases}", function(body)
    body = body:gsub("\\\\%[(%d+)mm%]", "\\\\\\noalign{\\vskip %1mm}")
    return "\\begin{cases}" .. body .. "\\end{cases}"
  end)
  if RTL then
    -- Persian words inside \text{…} must run right to left
    local out, pos = {}, 1
    while true do
      local a, b = s:find("\\text%s*{", pos)
      if not a then out[#out + 1] = s:sub(pos); break end
      out[#out + 1] = s:sub(pos, a - 1)
      local body, close = balanced(s, b)
      if not body then out[#out + 1] = s:sub(a); break end
      if has_arabic(body) then out[#out + 1] = "\\EMt{" .. body .. "}"
      else out[#out + 1] = s:sub(a, close) end
      pos = close + 1
    end
    s = table.concat(out)
  end
  return s
end

local function plain_math(s)    -- a bookmark-safe rendition of a formula
  s = s:gsub("\\operatorname%s*{(%a+)}", "%1"):gsub("\\mathrm%s*{(%a+)}", "%1")
  return (s:gsub("[\\{}$^_]", ""))
end


-- places where a displayed formula may be broken: before a top-level =, \Rightarrow, ...,
-- after \qquad / \quad.  Anything inside braces, \left..\right or an environment is left alone.
local BREAK_BEFORE = { Rightarrow = true, Longrightarrow = true, Longleftrightarrow = true,
                       implies = true, iff = true, approx = true, cong = true }
local BREAK_AFTER = { qquad = true, quad = true }
local function split_top(s)
  local out, i, n = {}, 1, #s
  local depth, env = 0, 0
  while i <= n do
    local c = s:sub(i, i)
    if c == "\\" then
      local name = s:match("^\\(%a+)", i)
      if name then
        if name == "begin" or name == "left" then env = env + 1
        elseif name == "end" or name == "right" then env = env - 1 end
        if depth == 0 and env == 0 and BREAK_BEFORE[name] and i > 1 then out[#out + 1] = "\\EMbr " end
        out[#out + 1] = "\\" .. name
        i = i + #name + 1
        if depth == 0 and env == 0 and BREAK_AFTER[name] then out[#out + 1] = "\\EMbr " end
      else
        out[#out + 1] = s:sub(i, i + 1); i = i + 2
      end
    else
      if c == "{" then depth = depth + 1
      elseif c == "}" then depth = depth - 1 end
      if c == "=" and depth == 0 and env == 0 and i > 1 then out[#out + 1] = "\\EMbr " end
      out[#out + 1] = c; i = i + 1
    end
  end
  return table.concat(out)
end

-- inline rendering -----------------------------------------------------------
local ESC = { ["&"] = "\\&", ["%"] = "\\%", ["#"] = "\\#", ["_"] = "\\_",
              ["{"] = "\\{", ["}"] = "\\}", ["~"] = "\\textasciitilde{}",
              ["^"] = "\\textasciicircum{}", ["\\"] = "\\textbackslash{}" }
local function esc(s) return (s:gsub("[&%%#_{}~^\\]", ESC)) end

local function classify(el)
  if el.t == "Str" then
    if has_latin(el.text) and not has_arabic(el.text) then return "L" end
    return "O"
  elseif el.t == "Space" or el.t == "SoftBreak" then return "S" end
  return "O"
end

-- Persian text: a run of Latin words stays in one left-to-right group
local function group_latin(inlines)
  local out, i, n = pandoc.List(), 1, #inlines
  while i <= n do
    if classify(inlines[i]) == "L" then
      local j = i
      while j + 2 <= n and classify(inlines[j + 1]) == "S" and classify(inlines[j + 2]) == "L" do
        j = j + 2
      end
      local words = {}
      for k = i, j do
        words[#words + 1] = inlines[k].t == "Str" and inlines[k].text or " "
      end
      local text = table.concat(words)
      local pre, core, post = text:match("^([^%w]*)(.-)([^%w]*)$")
      out:insert(raw(esc(pre) .. "\\lr{" .. esc(core) .. "}" .. esc(post)))
      i = j + 1
    else
      out:insert(inlines[i]); i = i + 1
    end
  end
  return out
end

local function inline_filter()
  local f = {}
  f.Math = function(el)
    if el.mathtype == "InlineMath" then
      return raw("\\EMim{" .. fix_math(el.text) .. "}")
    end
    return raw("\\EMdisp{" .. split_top(fix_math(el.text)) .. "}")
  end
  if RTL then f.Inlines = group_latin end
  return f
end
local IF = inline_filter()

local function render_inlines(inlines)
  local doc = pandoc.Pandoc({ pandoc.Plain(inlines) })
  doc = doc:walk(IF)
  local s = pandoc.write(doc, "latex")
  return (s:gsub("^%s+", ""):gsub("%s+$", ""))
end

local function markdown_inlines(text)
  local blocks = pandoc.read(text, "markdown-auto_identifiers").blocks
  if #blocks == 0 then return pandoc.List() end
  return blocks[1].content
end

local function plain_text(inlines)
  local t = {}
  inlines:walk({
    Str = function(e) t[#t + 1] = e.text end,
    Space = function() t[#t + 1] = " " end,
    Math = function(e) t[#t + 1] = plain_math(e.text) end,
  })
  return (table.concat(t):gsub("[\\{}]", ""))
end

---------------------------------------------------------------------------
-- blocks
---------------------------------------------------------------------------
function Header(h)
  if h.level == 1 then return {} end            -- the chapter title is set by the build
  local title = render_inlines(h.content)
  local plain = plain_text(h.content)
  local macro = h.level == 2 and "\\EMsection" or "\\EMsubsection"
  return rawb(macro .. "{" .. title .. "}{" .. plain .. "}")
end

function Div(el)
  for _, c in ipairs(el.classes) do
    local env = ENVS[c]
    if env then
      local title = el.attributes.title or ""
      local t = title ~= "" and render_inlines(markdown_inlines(title)) or ""
      local out = pandoc.List({ rawb("\\begin{" .. env .. "}{" .. t .. "}") })
      out:extend(el.content)
      out:insert(rawb("\\end{" .. env .. "}"))
      return out
    end
    local open = OPEN_ENVS[c]
    if open then
      local out = pandoc.List({ rawb("\\begin{" .. open .. "}") })
      out:extend(el.content)
      out:insert(rawb("\\end{" .. open .. "}"))
      return out
    end
  end
end

local function file_exists(p)
  local f = io.open(p, "r")
  if f then f:close() return true end
  return false
end

function CodeBlock(el)
  if not el.classes:includes("figure") then return nil end
  local name = el.identifier
  local cap = el.attributes.caption or ""
  local tex = cap ~= "" and render_inlines(markdown_inlines(cap)) or ""
  if not file_exists(FIGDIR .. "/" .. name .. ".tex") then
    io.stderr:write("md2tex: missing figure file " .. name .. ".tex\n")
    return rawb("\\fbox{missing figure " .. name .. "}")
  end
  return rawb("\\EMfigure{" .. name .. "}{" .. tex .. "}")
end

-- keeping logical blocks together ---------------------------------------------------
-- Outside the boxes the body is cut into "units": a paragraph with the equations, figures and
-- lists that follow it (a figure is attached to a short lead-in only).  A unit is measured by
-- the template and, when it fits on a page, never split between two pages.  A heading is held
-- back until the box or unit after it has decided where it goes.
local BOXENV = { EMdefinition = true, EMtheorem = true, EMexample = true, EMexercise = true,
                  EMimportant = true, EMremark = true, EMproof = true, EMsolution = true,
                  EMlemma = true, EMproposition = true, EMcorollary = true }
local function rawtext(b) return b.t == "RawBlock" and b.text or "" end
local function is_head(b) local s = rawtext(b); return s:match("^\\EMsection") or s:match("^\\EMsubsection") end
local function is_fig(b) return rawtext(b):match("^\\EMfigure{") ~= nil end
local function is_disp(b)
  if b.t ~= "Para" then return false end
  local n = 0
  for _, x in ipairs(b.content) do
    if x.t == "RawInline" and x.text:match("^\\EMdisp{") then n = n + 1
    elseif x.t ~= "SoftBreak" and x.t ~= "Space" then return false end
  end
  return n > 0
end
local function kind(b)
  if is_fig(b) then return "fig" end
  if is_disp(b) then return "disp" end
  if b.t == "Para" then return "text" end
  if b.t == "BulletList" or b.t == "OrderedList" then return "list" end
  return "other"
end
local function group_units(doc)
  local blocks, out, depth = doc.blocks, pandoc.List(), 0
  local cur, curtext, curhead = {}, 0, false
  local function flush()
    if #cur == 0 then return end
    local rich = #cur > 1 or kind(cur[1]) ~= "text"
    if rich then out:insert(rawb("\\begin{EMunit}")) end
    for _, x in ipairs(cur) do out:insert(x) end
    if rich then out:insert(rawb("\\end{EMunit}")) end
    cur, curtext = {}, 0
  end
  for _, b in ipairs(blocks) do
    local s = rawtext(b)
    local benv = s:match("^\\begin{(EM%a+)}")
    if benv and BOXENV[benv] then
      if depth == 0 then flush() end
      depth = depth + 1; out:insert(b)
    elseif s:match("^\\end{(EM%a+)}") and BOXENV[s:match("^\\end{(EM%a+)}")] then
      depth = depth - 1; out:insert(b)
    elseif depth > 0 then out:insert(b)
    else
      local k = kind(b)
      if k == "other" then flush(); out:insert(b)
      elseif k == "text" then
        -- a short lead-in (right after a heading, or ending in a colon) stays with what follows
        if #cur == 1 and kind(cur[1]) == "text" and curtext < 260
           and (curhead or pandoc.utils.stringify(cur[1]):match(":%s*$")) then
          cur[#cur + 1] = b; curtext = #pandoc.utils.stringify(b); curhead = false
        else
          flush(); curhead = #out > 0 and is_head(out[#out]) and true or false
          cur = { b }; curtext = #pandoc.utils.stringify(b)
        end
      elseif k == "fig" then
        if #cur > 0 and curtext >= 420 then flush() end
        cur[#cur + 1] = b
      else cur[#cur + 1] = b end   -- disp, list
      if k == "fig" then curtext = 0 end
    end
  end
  flush()
  -- a unit directly followed by a proof is joined to it
  do
    local joined, i = pandoc.List(), 1
    while i <= #out do
      local b = out[i]
      if rawtext(b) == "\\end{EMunit}" and out[i + 1] and rawtext(out[i + 1]):match("^\\begin{EMproof}") then
        -- find the matching \begin{EMunit} already emitted, and put the join before it
        local k = #joined
        while k > 0 and rawtext(joined[k]) ~= "\\begin{EMunit}" do k = k - 1 end
        if k > 0 then
          joined:insert(k, rawb("\\begin{EMjoin}"))
          joined:insert(b)
          local d = 0; local j = i + 1
          while out[j] do
            joined:insert(out[j])
            local s = rawtext(out[j])
            if s:match("^\\begin{EMproof}") then d = d + 1 elseif s:match("^\\end{EMproof}") then d = d - 1 end
            j = j + 1
            if d == 0 then break end
          end
          joined:insert(rawb("\\end{EMjoin}"))
          i = j
        else joined:insert(b); i = i + 1 end
      else joined:insert(b); i = i + 1 end
    end
    out = joined
  end
  -- a heading before a box or a unit is held until that block has measured itself
  local res = pandoc.List()
  local i = 1
  while i <= #out do
    if is_head(out[i]) then
      local j = i
      while out[j + 1] and is_head(out[j + 1]) do j = j + 1 end
      local nb = out[j + 1]
      local s = nb and rawtext(nb) or ""
      local benv = s:match("^\\begin{(EM%a+)}")
      if benv and (benv == "EMunit" or benv == "EMjoin" or BOXENV[benv]) then res:insert(rawb("\\EMhold")) end
      for k = i, j do res:insert(out[k]) end
      i = j + 1
    else res:insert(out[i]); i = i + 1 end
  end
  doc.blocks = res
  return doc
end

-- phases: blocks first, top-down (headers need their original inlines for the
-- bookmark-safe plain title), then the inline conversion, then the keep-together guards
return {
  { traverse = "topdown", Header = Header, Div = Div, CodeBlock = CodeBlock },
  IF,
  { Pandoc = group_units },
}
