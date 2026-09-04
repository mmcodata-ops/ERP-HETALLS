with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'const interval = setInterval(() => fetchAll(false), 5000);' in line:
        continue
    if 'clearInterval(interval);' in line:
        continue
    if 'interval = setInterval(() => {' in line:
        new_lines.append(line.replace('interval = setInterval(() => {', '// interval = setInterval(() => {'))
        continue
    if '}, 15000);' in line:
        new_lines.append(line.replace('}, 15000);', '// }, 15000);'))
        continue
    new_lines.append(line)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
