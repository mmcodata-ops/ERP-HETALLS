import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

target = "top: 60px !important; /* Touch the upper side of the bars */"
replacement = "top: 0px !important; /* Touch the upper side of the bars (relative to chart wrapper) */"

css = css.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Adjusted top to 0px")
