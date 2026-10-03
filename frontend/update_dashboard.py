import sys
import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r"<div style=\{\{\s*display:\s*'flex',\s*background:\s*'var\(--bg-card\)',.*?</div>"

new_hgho = """<div className="dock-container" style={{ flexShrink: 0 }}>
                <button onClick={() => setChartView('hg')} className={`dock-tab ${chartView === 'hg' ? 'active' : ''}`}>H.G.</button>
                <button onClick={() => setChartView('ho')} className={`dock-tab ${chartView === 'ho' ? 'active' : ''}`}>H.O.</button>
              </div>"""

text, count = re.subn(pattern, new_hgho, text, flags=re.DOTALL)
if count > 0:
    with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated Dashboard.jsx successfully with flexible regex.")
else:
    print("Could not find the target string in Dashboard.jsx")
