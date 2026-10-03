import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Pass chartView to Tooltip
content = content.replace('<Tooltip content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} />}',
                          '<Tooltip content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />}')

# Update Tooltip definition
content = content.replace('const ProgressChartTooltip = ({ active, payload, label, data, hoveredDataKey, tooltipLocked }) => {',
                          'const ProgressChartTooltip = ({ active, payload, label, data, hoveredDataKey, tooltipLocked, chartView }) => {')

content = content.replace("const salesCountItem = payload.find(p => p.dataKey === 'order_count')",
                          "const salesCountItem = payload.find(p => p.dataKey === (chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'))")

content = content.replace("const portalItems = payload.filter(p => p.dataKey !== 'order_count' && p.dataKey !== 'month' && p.dataKey !== '_dt')",
                          "const portalItems = payload.filter(p => p.dataKey !== 'order_count_hg' && p.dataKey !== 'order_count_ho' && p.dataKey !== 'month' && p.dataKey !== '_dt')")

# Fix YAxis and Line in ComposedChart
content = content.replace("{chartView === 'hg' && <YAxis yAxisId=\"right\"", "<YAxis yAxisId=\"right\"")
content = content.replace("offset: 5 }} />}", "offset: 5 }} />")

content = content.replace("{chartView === 'hg' && <Line isAnimationActive={false} yAxisId=\"right\" type=\"linear\" dataKey=\"order_count\"",
                          "<Line isAnimationActive={false} yAxisId=\"right\" type=\"linear\" dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'}")
content = content.replace("activeDot={{ r: 6, fill: '#ef4444', stroke: '#fff' }} />}", "activeDot={{ r: 6, fill: '#ef4444', stroke: '#fff' }} />")

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Dashboard.jsx")
