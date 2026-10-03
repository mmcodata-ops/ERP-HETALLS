import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace Body and remove overlay
pattern_body = r"body\s*\{[^\}]*position:\s*relative;[^\}]*z-index:\s*0;\s*\}\s*body::before\s*\{[^\}]*z-index:\s*-1;\s*\}"

new_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #050811; /* Deep navy base */
  background-image: 
    radial-gradient(at 0% 0%, rgba(79, 70, 229, 0.15) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.15) 0px, transparent 50%),
    radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.1) 0px, transparent 50%),
    radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.1) 0px, transparent 50%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""

css, count = re.subn(pattern_body, new_body, css, flags=re.DOTALL)
if count == 0:
    print("Warning: could not match body block. Using fallback replace.")
    # Fallback if exact match fails
    css = re.sub(r"body\s*\{.*?-webkit-font-smoothing:\s*antialiased;.*?\}", new_body, css, flags=re.DOTALL)
    css = re.sub(r"body::before\s*\{.*?z-index:\s*-1;\s*\}", "", css, flags=re.DOTALL)

# 2. Update the backgrounds of cards to 0.03 opacity so they are visible on dark
def boost_opacity(text):
    return text.replace("background: rgba(255, 255, 255, 0.01) !important;", "background: rgba(255, 255, 255, 0.03) !important;")

css = boost_opacity(css)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted to original dark background and adjusted card opacity.")
