import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the equiv selection with just previousDataRaw
target_tooltip = """  const isCurrentPeriod = currentIndex === data.length - 1
  const previousData = (isCurrentPeriod && previousDataRaw && previousDataRaw.equiv) ? previousDataRaw.equiv : previousDataRaw"""
replacement_tooltip = """  const isCurrentPeriod = currentIndex === data.length - 1
  const previousData = previousDataRaw"""
content = content.replace(target_tooltip, replacement_tooltip)

target_growth = """    const prevRaw = revenueChart[revenueChart.length - 2];
    const prev = (prevRaw && prevRaw.equiv) ? prevRaw.equiv : prevRaw;"""
replacement_growth = """    const prevRaw = revenueChart[revenueChart.length - 2];
    const prev = prevRaw;"""
content = content.replace(target_growth, replacement_growth)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Frontend equiv logic removed")
