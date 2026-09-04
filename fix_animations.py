import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Change the 15000 interval to 5000
content = re.sub(r'const interval = setInterval\(\(\) => fetchAll\(false\), \d+\);', 'const interval = setInterval(() => fetchAll(false), 5000);', content)
content = re.sub(r'// interval = setInterval', 'interval = setInterval', content)
content = re.sub(r'// }, 15000\); // Poll every 15 seconds', '}, 5000); // Poll every 5 seconds', content)

# Add isAnimationActive={false} to all Pie, Area, Bar, Line
content = re.sub(r'<Pie\s*\n', '<Pie isAnimationActive={false}\n', content)
content = re.sub(r'<Area\s+', '<Area isAnimationActive={false} ', content)
content = re.sub(r'<Bar\s+', '<Bar isAnimationActive={false} ', content)
content = re.sub(r'<Line\s+', '<Line isAnimationActive={false} ', content)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
