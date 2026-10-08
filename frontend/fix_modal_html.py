import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '</div>\n              <div className="breakdown-content">',
    '</div>\n            </div>\n              <div className="breakdown-content">'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added missing div")
