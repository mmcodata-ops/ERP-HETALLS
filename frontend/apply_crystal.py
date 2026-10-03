import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(pattern, repl):
    global css
    new_css, count = re.subn(pattern, repl, css, flags=re.DOTALL)
    if count == 0:
        print(f"Warning: could not match pattern {pattern[:30]}")
    return new_css

# 1. Lighten the dark overlay so the background image is HD and clear
css = safe_replace(r"body::before\s*\{[^\}]*background:\s*rgba\(5,\s*8,\s*17,\s*0\.4\);[^\}]*\}", 
"""body::before {
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.15); /* Much lighter overlay for HD clarity */
  z-index: -1;
}""")

# Crystal glass definition
crystal_bg = "rgba(255, 255, 255, 0.01)" # Extremely clear
crystal_blur = "blur(12px) saturate(120%)" # Lower blur for "HD" transparency
crystal_shadow = "0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.15), inset 0 1px 2px rgba(255, 255, 255, 0.3)"
crystal_borders = """  border: none !important;""" # Use inner shadow instead for a sharper edge

def replace_glass(css_text, selector, radius):
    pattern = r"(" + re.escape(selector) + r"\s*\{)(.*?)(\})"
    def repl(m):
        inner = m.group(2)
        inner = re.sub(r'background:.*?;', '', inner)
        inner = re.sub(r'backdrop-filter:.*?;', '', inner)
        inner = re.sub(r'-webkit-backdrop-filter:.*?;', '', inner)
        inner = re.sub(r'border.*?:.*?;', '', inner)
        inner = re.sub(r'box-shadow:.*?;', '', inner)
        inner = re.sub(r'border-radius:.*?;', '', inner)
        
        new_props = f"""
  background: {crystal_bg} !important;
  backdrop-filter: {crystal_blur} !important;
  -webkit-backdrop-filter: {crystal_blur} !important;
  border-radius: {radius} !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.35) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.25) !important;
  box-shadow: {crystal_shadow} !important;
"""
        return m.group(1) + new_props + inner + m.group(3)
    return re.sub(pattern, repl, css_text, flags=re.DOTALL)

css = replace_glass(css, ".kpi-card", "24px")
css = replace_glass(css, ".card", "24px")
css = replace_glass(css, ".login-card", "24px")
css = replace_glass(css, ".breakdown-table-wrapper", "24px")
css = replace_glass(css, ".sidebar", "0")
css = replace_glass(css, ".header", "0")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Ultra HD Crystal Clear Theme")
