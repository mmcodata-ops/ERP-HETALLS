import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("grid-template-columns: repeat(1, 1fr) !important;", "grid-template-columns: repeat(2, 1fr) !important;")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored 2 columns on mobile.")
