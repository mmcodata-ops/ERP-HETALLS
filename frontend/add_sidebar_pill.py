import sys
import re

with open('frontend/src/components/Sidebar.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add useRef, useEffect, useLocation
imports = "import React, { useRef, useEffect, useState } from 'react'\nimport { NavLink, useNavigate, useLocation } from 'react-router-dom'"
code = re.sub(r"import React from 'react'\nimport { NavLink, useNavigate } from 'react-router-dom'", imports, code)

# Inject logic to Sidebar component
logic = """
  const location = useLocation()
  const navRef = useRef(null)
  const [pillStyle, setPillStyle] = useState({ opacity: 0, top: 0, height: 0 })

  useEffect(() => {
    // Wait a tick for render
    setTimeout(() => {
      if (!navRef.current) return
      const activeEl = navRef.current.querySelector('.nav-item.active')
      if (activeEl) {
        setPillStyle({
          opacity: 1,
          top: activeEl.offsetTop,
          height: activeEl.offsetHeight
        })
      } else {
        setPillStyle(p => ({ ...p, opacity: 0 }))
      }
    }, 50)
  }, [location.pathname])
"""
code = code.replace("const initials = user?.name", logic + "\n  const initials = user?.name")

# Add the pill element and ref to nav
code = code.replace('<nav className="sidebar-nav">', '<nav className="sidebar-nav" ref={navRef} style={{ position: "relative" }}>\n          <div className="active-pill" style={{ position: "absolute", left: 12, right: 12, top: pillStyle.top, height: pillStyle.height, opacity: pillStyle.opacity, background: "rgba(255, 255, 255, 0.1)", borderRadius: "50px", transition: "all 0.4s cubic-bezier(0.34, 1.4, 0.64, 1)", zIndex: 0 }} />')

# Ensure nav-items have zIndex > 0
code = code.replace('className={({ isActive }) => `nav-item${isActive ? \' active\' : \'\'}`}', 'className={({ isActive }) => `nav-item${isActive ? \' active\' : \'\'}`} style={{ position: "relative", zIndex: 1 }}')

with open('frontend/src/components/Sidebar.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Added sliding pill to sidebar.")
