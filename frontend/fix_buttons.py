import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """              <div className="glass-switch" data-v={chartGroupBy}>
                <span className="glass-switch-knob" />
                <button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Mo</button>
                <button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Wk</button>
                <button className={chartGroupBy === 'day' ? 'on' : ''} onClick={() => setChartGroupBy('day')}>Dy</button>
              </div>"""

replacement = """              <div className="glass-switch" data-v={chartGroupBy}>
                <span className="glass-switch-knob" />
                <button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Month</button>
                <button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Week</button>
              </div>"""

content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard.jsx buttons fixed to 2 options")
