import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove flex: 1 from .kpi-card
css = re.sub(r"flex:\s*1;", "", css)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed flex: 1 from .kpi-card")
