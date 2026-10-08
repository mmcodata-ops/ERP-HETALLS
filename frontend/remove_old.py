import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Use regex to remove the old block
css = re.sub(
    r'/\* --- STATIC BREAKDOWN CARD HEIGHT FIX ---\*/\s*\.breakdown-static-card,\s*\.breakdown-static-card \.kpi-card \{[^}]+\}\s*@media \(max-width: 900px\) \{\s*\.breakdown-static-card,\s*\.breakdown-static-card \.kpi-card \{[^}]+\}\s*\}',
    '',
    css,
    flags=re.MULTILINE
)

# wait, the comment was /* --- STATIC BREAKDOWN CARD HEIGHT FIX --- */
css = re.sub(
    r'/\* --- STATIC BREAKDOWN CARD HEIGHT FIX ---\s*\*/\s*\.breakdown-static-card,\s*\.breakdown-static-card \.kpi-card\s*\{[^}]+\}\s*@media\s*\(max-width:\s*900px\)\s*\{\s*\.breakdown-static-card,\s*\.breakdown-static-card \.kpi-card\s*\{[^}]+\}\s*\}',
    '',
    css,
    flags=re.MULTILINE
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Removed old block")
