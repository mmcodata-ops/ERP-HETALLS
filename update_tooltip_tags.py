import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<Tooltip wrapperClassName="mobile-fixed-tooltip" content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />',
    '<Tooltip wrapperClassName="mobile-fixed-tooltip" content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} chartGroupBy={chartGroupBy} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
