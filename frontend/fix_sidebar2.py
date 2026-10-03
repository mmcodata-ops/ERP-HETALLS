import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

old_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: #060913 !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.7) !important;
  display: flex;"""
new_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: rgba(255, 255, 255, 0.02) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.4) !important;
  display: flex;"""
safe_replace(old_sidebar, new_sidebar)

old_header = """.header {
  height: var(--header-height);
  background: #080d1a !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.6) !important;
  display: flex; align-items: center; justify-content: space-between;"""
new_header = """.header {
  height: var(--header-height);
  background: rgba(255, 255, 255, 0.02) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4) !important;
  display: flex; align-items: center; justify-content: space-between;"""
safe_replace(old_header, new_header)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Safely replaced CSS sidebar/header")
