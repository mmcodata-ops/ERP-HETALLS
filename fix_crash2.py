import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"const \[revenueChartMtd, setRevenueChartMtd\] = useState\(null\)"
replacement = """const [revenueChartMtd, setRevenueChartMtd] = useState(null)
  const revenueChart = chartGroupBy === 'month' ? revenueChartMonth : revenueChartMtd;"""

content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
