import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace overflow-x: hidden with overflow: visible in .kpi-grid overrides
css = re.sub(r'overflow-x:\s*hidden;?', 'overflow: visible !important;', css)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Changed overflow to visible on .kpi-grid to fix tooltip clipping.")
