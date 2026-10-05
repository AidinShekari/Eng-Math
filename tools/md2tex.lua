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
}
local OPEN_ENVS = { proof = "EMproof", solution = "EMsolution" }

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

-- a heading that is followed by a figure (directly, or after one short paragraph) stays
-- with it: the guard reserves the room for the heading, the paragraph and the drawing
local BOXENV = { EMdefinition = true, EMtheorem = true, EMexample = true, EMexercise = true,
                  EMimportant = true, EMremark = true }
local function keep_heading_with_figure(doc)
  local blocks, out, i = doc.blocks, pandoc.List(), 1
  local function head(b) return b.t == "RawBlock" and (b.text:match("^\\EMsection") or b.text:match("^\\EMsubsection")) end
  local function fig(b) return b.t == "RawBlock" and b.text:match("^\\EMfigure{([^}]*)}") end
  while i <= #blocks do
    local b = blocks[i]
    if head(b) then
      local nxt, name, extra = blocks[i + 1], nil, 3
      if nxt then name = fig(nxt) end
      if not name and nxt and nxt.t == "Para" and #pandoc.utils.stringify(nxt) < 260 then
        local nn = blocks[i + 2]
        if nn then name = fig(nn); extra = 5 end
      end
      if name then out:insert(rawb("\\EMkeepfig{" .. name .. "}{" .. extra .. "}")) end
      -- a heading (or a run of headings) followed by a box is held until the box has measured itself
      if not name and nxt and nxt.t == "Para" and #nxt.content == 1 and nxt.content[1].t == "Math"
         and nxt.content[1].mathtype == "DisplayMath" then
        local _, rows = nxt.content[1].text:gsub("\\\\", "")
        out:insert(rawb("\\Needspace{" .. (7 + 2 * rows) .. "\\baselineskip}"))
      end
      local j = i + 1
      while blocks[j] and head(blocks[j]) do j = j + 1 end
      local nb = blocks[j]
      local benv = nb and nb.t == "RawBlock" and nb.text:match("^\\begin{(EM%a+)}")
      if not name and benv and BOXENV[benv] then
        out:insert(rawb("\\EMhold"))
      end
    end
    out:insert(b); i = i + 1
  end
  doc.blocks = out
  return doc
end

-- phases: blocks first, top-down (headers need their original inlines for the
-- bookmark-safe plain title), then the inline conversion, then the keep-together guards
return {
  { traverse = "topdown", Header = Header, Div = Div, CodeBlock = CodeBlock },
  IF,
  { Pandoc = keep_heading_with_figure },
}
