import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix sidebar — flush to left edge, no floating pill, no glass
old_sidebar = re.search(r'\/\* .+ Sidebar .+\*\/\n\.sidebar \{[^}]+\}', css)
if old_sidebar:
    new_sidebar = """/* Sidebar */
.sidebar {
  background: rgba(10, 12, 20, 0.95) !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border-radius: 0 !important;
  border: none !important;
  border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
  box-shadow: none !important;

  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  
  display: flex;
  flex-direction: column;
  z-index: 100;
  overflow-y: auto;
}"""
    css = css[:old_sidebar.start()] + new_sidebar + css[old_sidebar.end():]

# 2. Fix nav-item active state — simple dark rounded rectangle, no glass pill
nav_active = """.nav-item.active {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  color: #ffffff !important;
}"""

# Replace existing active state
css = re.sub(r'\.nav-item\.active\s*\{[^}]+\}', nav_active, css)

# 3. Fix dock-container (H.G./H.O. toggle) — simple dark capsule
old_dock = re.search(r'\.dock-container\s*\{[^}]+\}', css)
if old_dock:
    new_dock = """.dock-container {
  display: inline-flex;
  align-items: center;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 3px;
  gap: 2px;
}"""
    css = css[:old_dock.start()] + new_dock + css[old_dock.end():]

# 4. Fix dock-tab styling — simple, clean
old_tab = re.search(r'\.dock-tab\s*\{[^}]+\}', css)
if old_tab:
    new_tab = """.dock-tab {
  padding: 6px 16px;
  border-radius: 10px;
  border: none;
  background: transparent;
  color: rgba(255, 255, 255, 0.5);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}"""
    css = css[:old_tab.start()] + new_tab + css[old_tab.end():]

# 5. Fix dock-tab active — simple dark pill, no glass
old_tab_active = re.search(r'\.dock-tab\.active\s*\{[^}]+\}', css)
if old_tab_active:
    new_tab_active = """.dock-tab.active {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.1);
}"""
    css = css[:old_tab_active.start()] + new_tab_active + css[old_tab_active.end():]

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied clean minimal sidebar and toggle styling.")
