import os

file_path = 'frontend/src/pages/Forecast.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('stroke="var(--primary-color)"', 'stroke="#3b82f6" isAnimationActive={false}')
content = content.replace('stroke="var(--success-color)"', 'stroke="#10b981" isAnimationActive={false}')
content = content.replace("fill: 'var(--primary-color)'", "fill: '#3b82f6'")
content = content.replace("fill: 'var(--success-color)'", "fill: '#10b981'")

# While we are here, let's make sure the data values are definitely numbers, not strings or undefined
content = content.replace("cumulative += dayTotal", "cumulative += (dayTotal || 0)")
content = content.replace("const targetTrajectory = (target / totalDays) * i", "const targetTrajectory = ((target || 0) / (totalDays || 1)) * i")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Recharts colors")
