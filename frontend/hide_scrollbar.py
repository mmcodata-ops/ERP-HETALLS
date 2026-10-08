import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add scrollbar hiding for breakdown-tabs-container
if '.breakdown-tabs-container' not in css:
    css += "\n.breakdown-tabs-container::-webkit-scrollbar { display: none; }\n.breakdown-tabs-container { -ms-overflow-style: none; scrollbar-width: none; }\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Scrollbar hidden for container")
