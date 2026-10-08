import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Exclude 'equiv' from allChartPortals
target1 = """if (key !== "month" && key !== "total" && key !== "_dt" && key !== "order_count" && key !== "order_count_hg" && key !== "order_count_ho") {"""
replacement1 = """if (key !== "month" && key !== "total" && key !== "_dt" && key !== "order_count" && key !== "order_count_hg" && key !== "order_count_ho" && key !== "equiv") {"""
content = content.replace(target1, replacement1)

# 2. Exclude 'equiv' from tooltip total calculations
target2 = """const skipKeys = new Set(['order_count', 'order_count_hg', 'order_count_ho', 'month', '_dt', 'total']);"""
replacement2 = """const skipKeys = new Set(['order_count', 'order_count_hg', 'order_count_ho', 'month', '_dt', 'total', 'equiv']);"""
content = content.replace(target2, replacement2)

# 3. Change "Week" to "Date" / "Day" in the toggle UI
target3 = """<div className="card-title">{chartGroupBy === 'week' ? 'Weekly' : 'Monthly'} Revenue Trend</div>"""
replacement3 = """<div className="card-title">{chartGroupBy === 'day' ? 'Date-Wise' : 'Monthly'} Revenue Trend</div>"""
content = content.replace(target3, replacement3)

target4 = """<button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Week</button>"""
replacement4 = """<button className={chartGroupBy === 'day' ? 'on' : ''} onClick={() => setChartGroupBy('day')}>Date</button>"""
content = content.replace(target4, replacement4)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Frontend patched")
