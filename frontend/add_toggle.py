import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """          <div className="card">
            <div className="card-header">
              <div>
                <div className="card-title">Monthly Revenue Trend</div>
                <div className="card-subtitle">{chartView === 'ho' ? 'Hetalls Only — Monthly Brands' : 'All Companies — Monthly Brands'}</div>
              </div>
            </div>"""

replacement = """          <div className="card">
            <div className="card-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div>
                <div className="card-title">{chartGroupBy === 'week' ? 'Weekly' : 'Monthly'} Revenue Trend</div>
                <div className="card-subtitle">{chartView === 'ho' ? 'Hetalls Only — Trend' : 'All Companies — Trend'}</div>
              </div>
              <div className="glass-switch" data-v={chartGroupBy}>
                <span className="glass-switch-knob" />
                <button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Month</button>
                <button className={chartGroupBy === 'week' ? 'on' : ''} onClick={() => setChartGroupBy('week')}>Week</button>
              </div>
            </div>"""

new_content = content.replace(target, replacement)

if target in content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Toggle added successfully.")
else:
    print("Target not found! Let's find exactly what it looks like.")
