import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = 'sub="Growth vs Last Month"'
replacement = 'sub="Growth vs Previous"'
content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated sub text")
