import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add wrapperClassName to BarChart tooltips
target = """<Tooltip content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />"""
replacement = """<Tooltip wrapperClassName="mobile-fixed-tooltip" content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />"""
content = content.replace(target, replacement)

target2 = """<Tooltip content={<ProgressChartTooltip data={hetallsChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />"""
replacement2 = """<Tooltip wrapperClassName="mobile-fixed-tooltip" content={<ProgressChartTooltip data={hetallsChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />"""
content = content.replace(target2, replacement2)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("wrapperClassName added to tooltips")
