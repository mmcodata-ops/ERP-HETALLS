import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the replacement for previousData logic
target = """  const currentIndex = data.findIndex(d => d.month === label)
  const previousData = currentIndex > 0 ? data[currentIndex - 1] : null"""

replacement = """  const currentIndex = data.findIndex(d => d.month === label)
  const previousDataRaw = currentIndex > 0 ? data[currentIndex - 1] : null
  const isCurrentPeriod = currentIndex === data.length - 1
  const previousData = (isCurrentPeriod && previousDataRaw && previousDataRaw.equiv) ? previousDataRaw.equiv : previousDataRaw"""

content = content.replace(target, replacement)

# Wait, the total calculation in the tooltip iterates over Object.entries(previousData)
# If previousData is previousDataRaw.equiv, it only contains portal keys and order_count, not month and _dt.
# The skipKeys set in the total calculation handles keys it doesn't care about, so that's fine.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("ProgressChartTooltip logic updated")
