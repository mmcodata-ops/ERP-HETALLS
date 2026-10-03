import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

# 1. Update Body to a high-end cinematic abstract fluid image
old_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #050811; /* Deep navy base */
  background-image: 
    radial-gradient(at 0% 0%, rgba(79, 70, 229, 0.2) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.2) 0px, transparent 50%),
    radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.15) 0px, transparent 50%),
    radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.15) 0px, transparent 50%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""

new_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #050811;
  background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  position: relative;
  z-index: 0;
}
body::before {
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(5, 8, 17, 0.4); /* Dark overlay to keep text readable while letting colors pop */
  z-index: -1;
}"""
safe_replace(old_body, new_body)

# 2. Refine cards for TRUE glass refraction now that we have a background
# The previous cards had a linear gradient that blocked too much background. We need highly transparent cards.
true_glass_bg = "rgba(255, 255, 255, 0.02)"
true_glass_blur = "blur(24px) saturate(180%)"
true_glass_shadow = "0 15px 35px rgba(0, 0, 0, 0.4), inset 0 2px 3px rgba(255, 255, 255, 0.2)"
true_glass_borders = """  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.2) !important;"""

# We'll use regex to replace the glass properties in the cards so we don't rely on exact string matches of the old css
def apply_true_glass(css_string, selector, radius="24px", extra=""):
    pattern = r"(" + re.escape(selector) + r"\s*\{)[^\}]+(\})"
    
    # We want to keep padding, transition, etc. but replace background, filter, border, box-shadow.
    # It's easier to just do a precise replace for each block.
    pass

# Actually, I'll just regex replace the specific properties inside each known class to be safe.
def replace_props(css_text, selector, radius):
    pattern = r"(" + re.escape(selector) + r"\s*\{)(.*?)(\})"
    def repl(m):
        inner = m.group(2)
        # Remove old background, blur, border, box-shadow, border-radius
        inner = re.sub(r'background:.*?;', '', inner)
        inner = re.sub(r'backdrop-filter:.*?;', '', inner)
        inner = re.sub(r'-webkit-backdrop-filter:.*?;', '', inner)
        inner = re.sub(r'border.*?:.*?;', '', inner)
        inner = re.sub(r'box-shadow:.*?;', '', inner)
        inner = re.sub(r'border-radius:.*?;', '', inner)
        
        new_props = f"""
  background: {true_glass_bg} !important;
  backdrop-filter: {true_glass_blur} !important;
  -webkit-backdrop-filter: {true_glass_blur} !important;
{true_glass_borders}
  border-radius: {radius} !important;
  box-shadow: {true_glass_shadow} !important;
"""
        return m.group(1) + new_props + inner + m.group(3)
    return re.sub(pattern, repl, css_text, flags=re.DOTALL)

css = replace_props(css, ".kpi-card", "24px")
css = replace_props(css, ".card", "24px")
css = replace_props(css, ".login-card", "24px")
css = replace_props(css, ".breakdown-table-wrapper", "24px")
css = replace_props(css, ".sidebar", "0")
css = replace_props(css, ".header", "0")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied cinematic background and true refraction glass!")
