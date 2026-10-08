import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace `left: 0, width: '100%'` with centered positioning
old_style = "position: 'absolute', top: '105%', left: 0, width: '100%', minWidth: '250px'"
new_style = "position: 'absolute', top: '105%', left: '50%', transform: 'translateX(-50%)', minWidth: '260px'"

content = content.replace(old_style, new_style)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated tooltips to be centered underneath the KPI cards.")
