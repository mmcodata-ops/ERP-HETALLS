import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add width: 100% to .kpi-card
if "width: 100% !important;" not in css.split(".kpi-card {")[1].split("}")[0]:
    css = css.replace(".kpi-card {\n    flex: 1 1 0 !important;", ".kpi-card {\n    flex: 1 1 0 !important;\n    width: 100% !important;")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Added width 100% to kpi-card")
