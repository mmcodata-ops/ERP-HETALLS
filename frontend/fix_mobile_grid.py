import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore @media (max-width: 1024px) for .kpi-grid
css = re.sub(
    r"@media\s*\(\s*max-width:\s*1024px\s*\)\s*\{.*?\.kpi-grid\s*\{[^\}]+\}",
    lambda m: m.group(0).replace("grid-template-columns: repeat(6, 1fr);", "grid-template-columns: repeat(3, 1fr);"),
    css,
    flags=re.DOTALL
)

# Restore @media (max-width: 768px) for .kpi-grid
css = re.sub(
    r"@media\s*\(\s*max-width:\s*768px\s*\)\s*\{.*?\.kpi-grid\s*\{[^\}]+\}",
    lambda m: m.group(0).replace("grid-template-columns: repeat(6, 1fr);", "grid-template-columns: repeat(2, 1fr);"),
    css,
    flags=re.DOTALL
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored mobile kpi-grid columns.")
