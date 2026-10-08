import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add const revenueChart inside Dashboard
pattern = r"const \[revenueChartMonth, setRevenueChartMonth\] = useState\(null\)\n  const \[revenueChartMtd, setRevenueChartMtd\] = useState\(null\)"

replacement = """const [revenueChartMonth, setRevenueChartMonth] = useState(null)
  const [revenueChartMtd, setRevenueChartMtd] = useState(null)
  const revenueChart = chartGroupBy === 'month' ? revenueChartMonth : revenueChartMtd;"""

content = content.replace(pattern, replacement)

# Revert ComposedChart and Tooltip to use revenueChart (since we defined it)
content = content.replace("data={(chartGroupBy === 'month' ? revenueChartMonth : revenueChartMtd) || []}", "data={revenueChart || []}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
