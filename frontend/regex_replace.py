import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div className="card-title">Monthly Revenue Trend</div>\s*<div className="card-subtitle">.*?</div>\s*</div>\s*</div>'

replacement = """<div className="card-title">{chartGroupBy === 'week' ? 'Weekly' : 'Monthly'} Revenue Trend</div>
              <div className="card-subtitle">{chartView === 'ho' ? 'Hetalls Only' : 'All Companies'} &mdash; Trend</div>
            </div>
            <div className="glass-switch" data-v={chartGroupBy}>
              <span className="glass-switch-knob" />
              <button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Month</button>
              <button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Week</button>
            </div>
          </div>"""

# Wait, we need to match from <div className="card-header"> to the end.
pattern_full = r'<div className="card-header">\s*<div>\s*<div className="card-title">Monthly Revenue Trend</div>\s*<div className="card-subtitle">.*?</div>\s*</div>\s*</div>'

replacement_full = """<div className="card-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
            <div>
              <div className="card-title">{chartGroupBy === 'week' ? 'Weekly' : 'Monthly'} Revenue Trend</div>
              <div className="card-subtitle">{chartView === 'ho' ? 'Hetalls Only' : 'All Companies'} &mdash; Trend</div>
            </div>
            <div className="glass-switch" data-v={chartGroupBy}>
              <span className="glass-switch-knob" />
              <button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Month</button>
              <button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Week</button>
            </div>
          </div>"""

new_content, count = re.subn(pattern_full, replacement_full, content)
print(f"Replaced {count} instances.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
