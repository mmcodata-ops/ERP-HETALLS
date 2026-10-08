import re

with open('frontend/src/components/Sidebar.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Remove the pill-tracking logic (useRef, useEffect, useState for pill, useLocation)
code = code.replace("import React, { useRef, useEffect, useState } from 'react'", "import React from 'react'")
code = code.replace("import { NavLink, useNavigate, useLocation } from 'react-router-dom'", "import { NavLink, useNavigate } from 'react-router-dom'")

# Remove the pill logic block
pill_logic = re.search(r'\n  const location = useLocation\(\).*?], \[location\.pathname\]\)', code, re.DOTALL)
if pill_logic:
    code = code[:pill_logic.start()] + code[pill_logic.end():]

# Remove the active-pill div element
pill_div = re.search(r'\s*<div className="active-pill"[^/]*/>', code)
if pill_div:
    code = code[:pill_div.start()] + code[pill_div.end():]

# Remove ref and style from nav
code = code.replace(' ref={navRef} style={{ position: "relative" }}', '')

# Remove inline style from NavLink
code = code.replace(' style={{ position: "relative", zIndex: 1 }}', '')

with open('frontend/src/components/Sidebar.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Removed sliding pill from sidebar — clean active states only.")
