import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find {old[:40]}")
    css = css.replace(old, new, count)

old_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #1a1c23; /* Solid dark grey/blue like the reference */
  background-image: none;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""

new_body = """body {
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
safe_replace(old_body, new_body)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Original Dashboard Background Restored")
