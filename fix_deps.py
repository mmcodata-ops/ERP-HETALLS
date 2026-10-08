import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The useEffect that fetches dashboard data has dependency array `[API]`
# We need to change it to `[API, chartGroupBy]`
content = re.sub(r'\}, \[API\]\);', r'}, [API, chartGroupBy]);', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
