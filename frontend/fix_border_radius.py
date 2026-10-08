import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace border-radius: 12px with 50px for .breakdown-tabs
css = re.sub(
    r'\.breakdown-tabs\s*\{([^}]*)border-radius:\s*12px\s*!important;',
    r'.breakdown-tabs {\1border-radius: 50px !important;',
    css
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Changed border-radius to 50px")
