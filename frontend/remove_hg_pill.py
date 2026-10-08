import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the complex sliding pill toggle with a simple toggle
old_toggle = """<div className="dock-container" style={{ flexShrink: 0, position: 'relative' }}>
                <div style={{
                  position: 'absolute',
                  top: 3, bottom: 3, width: 'calc(50% - 4px)',
                  background: 'linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.04))',
                  borderRadius: '14px',
                  border: '1px solid rgba(255,255,255,0.08)',
                  boxShadow: '0 4px 16px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.15)',
                  transition: 'transform 0.5s cubic-bezier(0.4, 0, 0, 1)',
                  transform: chartView === 'hg' ? 'translateX(3px)' : 'translateX(calc(100% + 5px))',
                  zIndex: 0
                }} />
                <button onClick={() => setChartView('hg')} className={`dock-tab ${chartView === 'hg' ? 'active' : ''}`} style={{ position: 'relative', zIndex: 1, background: 'transparent', border: 'none' }}>H.G.</button>
                <button onClick={() => setChartView('ho')} className={`dock-tab ${chartView === 'ho' ? 'active' : ''}`} style={{ position: 'relative', zIndex: 1, background: 'transparent', border: 'none' }}>H.O.</button>
              </div>"""

new_toggle = """<div className="dock-container" style={{ flexShrink: 0 }}>
                <button onClick={() => setChartView('hg')} className={`dock-tab ${chartView === 'hg' ? 'active' : ''}`}>H.G.</button>
                <button onClick={() => setChartView('ho')} className={`dock-tab ${chartView === 'ho' ? 'active' : ''}`}>H.O.</button>
              </div>"""

code = code.replace(old_toggle, new_toggle)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Simplified H.G./H.O. toggle — clean background swap.")
