import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we import LabelList if it's not already imported
if "LabelList" not in content:
    content = content.replace("LineChart, Line, ComposedChart,", "LineChart, Line, ComposedChart, LabelList,")

# We want to change the YAxis for the right side and add LabelList to the Line
# Old YAxis:
# <YAxis yAxisId="right" orientation="right" width={30} tick={{ fill: '#ef4444', fontSize: 11 }} axisLine={false} tickLine={false} />
# New YAxis:
# <YAxis yAxisId="right" orientation="right" width={30} tick={{ fill: '#ef4444', fontSize: 11 }} axisLine={false} tickLine={false} domain={[0, dataMax => Math.ceil(dataMax * 1.15)]} />

content = re.sub(
    r'<YAxis yAxisId="right" orientation="right" width=\{30\} tick=\{\{ fill: \'#ef4444\', fontSize: 11 \}\} axisLine=\{false\} tickLine=\{false\} />',
    r'<YAxis yAxisId="right" orientation="right" width={30} tick={{ fill: \'#ef4444\', fontSize: 11 }} axisLine={false} tickLine={false} domain={[0, dataMax => Math.ceil(dataMax * 1.15)]} />',
    content
)

# Old Line:
# <Line isAnimationActive={false} yAxisId="right" type="linear" dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'} name="Sales Count" stroke="#ef4444" strokeWidth={2} dot={{ r: 4, fill: '#ef4444', stroke: '#fff', strokeWidth: 1.5 }} activeDot={{ r: 6, fill: '#ef4444', stroke: '#fff' }} />
# New Line:
# <Line isAnimationActive={false} yAxisId="right" type="linear" dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'} name="Sales Count" stroke="#ef4444" strokeWidth={2} dot={{ r: 4, fill: '#ef4444', stroke: '#fff', strokeWidth: 1.5 }} activeDot={{ r: 6, fill: '#ef4444', stroke: '#fff' }}>
#   <LabelList dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'} position="top" offset={10} fill="#ef4444" fontSize={11} fontWeight="bold" />
# </Line>

old_line = r'<Line isAnimationActive=\{false\} yAxisId="right" type="linear" dataKey=\{chartView === \'ho\' \? \'order_count_ho\' : \'order_count_hg\'\} name="Sales Count" stroke="#ef4444" strokeWidth=\{2\} dot=\{\{ r: 4, fill: \'#ef4444\', stroke: \'#fff\', strokeWidth: 1\.5 \}\} activeDot=\{\{ r: 6, fill: \'#ef4444\', stroke: \'#fff\' \}\} />'
new_line = r"""<Line isAnimationActive={false} yAxisId="right" type="linear" dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'} name="Sales Count" stroke="#ef4444" strokeWidth={2} dot={{ r: 4, fill: '#ef4444', stroke: '#fff', strokeWidth: 1.5 }} activeDot={{ r: 6, fill: '#ef4444', stroke: '#fff' }}>
                  <LabelList dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'} position="top" offset={10} fill="#ef4444" fontSize={12} fontWeight="bold" />
                </Line>"""

content = re.sub(old_line, new_line, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard.jsx updated")
