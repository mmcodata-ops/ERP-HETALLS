import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the aggressive width: 100% from grid items that might be causing clipping/padding overflow
if "width: 100% !important;" in css.split(".kpi-grid > * {")[1]:
    # We replace the bulletproof mobile grid fix width rules
    css = css.replace(
        "width: 100% !important;\n      max-width: 100% !important;\n      justify-self: stretch !important;\n      align-self: stretch !important;\n      margin: 0 !important;",
        "justify-self: stretch !important;\n      align-self: stretch !important;\n      margin: 0 !important;"
    )

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed width 100% from kpi-grid children to restore padding")
