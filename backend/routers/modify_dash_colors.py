import re

with open('dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('''    colors = ["#f59e0b", "#3b82f6", "#ef4444", "#10b981", "#8b5cf6", "#ec4899", "#f87171", "#fb923c"]''', '''    colors = ["#f59e0b", "#3b82f6", "#ef4444", "#10b981", "#8b5cf6", "#ec4899", "#f87171", "#fb923c", "#14b8a6", "#eab308", "#0ea5e9", "#f97316", "#d946ef", "#06b6d4", "#84cc16", "#fef08a", "#fde68a", "#fecaca", "#bfdbfe"]''')

with open('dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
