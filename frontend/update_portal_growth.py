import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """    const latest = revenueChart[revenueChart.length - 1];
    const prev = revenueChart[revenueChart.length - 2];"""

replacement = """    const latest = revenueChart[revenueChart.length - 1];
    const prevRaw = revenueChart[revenueChart.length - 2];
    const prev = (prevRaw && prevRaw.equiv) ? prevRaw.equiv : prevRaw;"""

content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("PortalGrowthCard logic updated")
