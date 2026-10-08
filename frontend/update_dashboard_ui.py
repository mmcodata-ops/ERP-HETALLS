import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <div className="card-header">
              <div>
                <div className="card-title">Monthly Revenue Trend</div>
                <div className="card-subtitle">{chartView === 'ho' ? 'Hetalls Only — Monthly Brands' : 'All Companies — Monthly Brands'}</div>
              </div>
            </div>"""

replacement = """            <div className="card-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div>
                <div className="card-title">{chartGroupBy === 'week' ? 'Weekly' : chartGroupBy === 'day' ? 'Daily' : 'Monthly'} Revenue Trend</div>
                <div className="card-subtitle">{chartView === 'ho' ? 'Hetalls Only' : 'All Companies'} — Trend</div>
              </div>
              <div className="glass-switch" data-v={chartGroupBy}>
                <span className="glass-switch-knob" />
                <button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Mo</button>
                <button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Wk</button>
                <button className={chartGroupBy === 'day' ? 'on' : ''} onClick={() => setChartGroupBy('day')}>Dy</button>
              </div>
            </div>"""

content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added chartGroupBy toggle UI to Dashboard.jsx")
