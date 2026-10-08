import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace 100vw with 100% in mobile main-content to avoid scrollbar overflow issues
old_main = r"\.main-content\s*\{\s*margin-left: 0 !important;\s*width: 100vw !important;\s*max-width: 100vw !important;\s*box-sizing: border-box;\s*\}"
new_main = """.main-content {
      margin-left: 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box;
      overflow-x: hidden;
    }"""
css = re.sub(old_main, new_main, css)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed mobile main-content width to 100% instead of 100vw.")
