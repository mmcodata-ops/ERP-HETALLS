import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

frost_bg = "linear-gradient(110deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.05) 35%, rgba(255,255,255,0.01) 100%)"
frost_blur = "blur(16px) saturate(120%)"
frost_shadow = "0 10px 30px rgba(0, 0, 0, 0.2), inset 1px 1px 3px rgba(255, 255, 255, 0.4)"

# Sidebar
old_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: rgba(255, 255, 255, 0.04) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 15px 0 35px rgba(0, 0, 0, 0.3), inset -2px 0 5px rgba(255, 255, 255, 0.05) !important;
  display: flex;"""
new_sidebar = f""".sidebar {{
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: {frost_bg} !important;
  backdrop-filter: {frost_blur} !important;
  -webkit-backdrop-filter: {frost_blur} !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: {frost_shadow} !important;
  display: flex;"""
safe_replace(old_sidebar, new_sidebar)

# Header
old_header = """.header {
  height: var(--header-height);
  background: rgba(255, 255, 255, 0.04) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), inset 0 -2px 5px rgba(255, 255, 255, 0.05) !important;
  display: flex; align-items: center; justify-content: space-between;"""
new_header = f""".header {{
  height: var(--header-height);
  background: {frost_bg} !important;
  backdrop-filter: {frost_blur} !important;
  -webkit-backdrop-filter: {frost_blur} !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: {frost_shadow} !important;
  display: flex; align-items: center; justify-content: space-between;"""
safe_replace(old_header, new_header)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied frost styles to sidebar and header!")
