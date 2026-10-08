import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Increase the gap significantly for mobile
css = re.sub(
    r'margin: 12px 16px 8px 16px !important;',
    r'margin: 16px 16px 32px 16px !important;',
    css
)

css = re.sub(
    r'padding: 4px 16px 16px 16px !important;',
    r'padding: 12px 16px 16px 16px !important;',
    css
)

# Also ensure `.kpi-grid` has its own top margin if needed, but the header margin-bottom + page-body padding-top = 32+12 = 44px gap! This will definitely separate them.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Increased gap between header and kpi-grid")
