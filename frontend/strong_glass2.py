import sys
import re

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
  background: linear-gradient(to right, rgba(0,0,0,0.6) 0%, rgba(255,255,255,0.02) 100%) !important;
  backdrop-filter: blur(40px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 5px 0 45px rgba(0, 0, 0, 0.4) !important;
  display: flex;"""

new_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: linear-gradient(to right, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(40px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
  box-shadow: 10px 0 45px rgba(0, 0, 0, 0.5) !important;
  display: flex;"""
safe_replace(old_sidebar, new_sidebar)


old_header = """.header {
  height: var(--header-height);
  background: linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(30px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3) !important;
  display: flex; align-items: center; justify-content: space-between;"""

new_header = """.header {
  height: var(--header-height);
  background: linear-gradient(to bottom, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(30px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
  display: flex; align-items: center; justify-content: space-between;"""
safe_replace(old_header, new_header)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Sidebar & Header strong glass applied")
