import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure breakdown-table-wrapper has overflow-x: auto globally
if "overflow-x: auto !important;" not in css.split('.breakdown-table-wrapper {')[1].split('}')[0]:
    css = css.replace(".breakdown-table-wrapper {\n    background: rgba(255, 255, 255, 0.03) !important;", ".breakdown-table-wrapper {\n    overflow-x: auto !important;\n    -webkit-overflow-scrolling: touch;\n    background: rgba(255, 255, 255, 0.03) !important;")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Added overflow-x: auto globally to breakdown-table-wrapper")
