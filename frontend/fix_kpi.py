import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<KPICard icon={Layers} label="Detailed Breakdown" value="Breakdown" sub="Daily Sale Brands & Portal" colorClass="blue" format="text" />',
    '<KPICard icon={Layers} label="Detailed Breakdown" value="Breakdown" sub="Daily Sale Brands & Portal" colorClass="blue" format="text" style={{ flex: \'1 1 100%\', width: \'100%\', height: \'100%\', minHeight: \'100%\' }} />'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated KPICard style")
