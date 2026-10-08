import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'className="breakdown-tabs-container" style={{ width: \'100%\', overflowX: \'auto\', padding: \'0 24px\', marginBottom: \'16px\' }}',
    'className="breakdown-tabs-container" style={{ width: \'100%\', overflowX: \'auto\', padding: \'0 24px\', marginBottom: \'16px\', boxSizing: \'border-box\' }}'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added boxSizing")
