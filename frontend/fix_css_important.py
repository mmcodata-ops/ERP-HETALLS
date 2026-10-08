import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix mobile override for .breakdown-tabs
css = re.sub(
    r'\.breakdown-tabs\s*\{[^}]*width:\s*100%\s*!important;[^}]*\}',
    lambda m: m.group(0).replace('width: 100% !important;', 'width: max-content !important; min-width: 100% !important;'),
    css
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("index.css updated for width 100% important")
