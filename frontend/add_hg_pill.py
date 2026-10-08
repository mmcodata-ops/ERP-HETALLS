import sys
import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the dock-container with one that has a sliding pill
old_dock = """<div className="dock-container" style={{ flexShrink: 0 }}>
                <button onClick={() => setChartView('hg')} className={`dock-tab ${chartView === 'hg' ? 'active' : ''}`}>H.G.</button>
                <button onClick={() => setChartView('ho')} className={`dock-tab ${chartView === 'ho' ? 'active' : ''}`}>H.O.</button>
              </div>"""

new_dock = """<div className="dock-container" style={{ flexShrink: 0, position: 'relative' }}>
                <div style={{
                  position: 'absolute',
                  top: 4, bottom: 4, width: 'calc(50% - 4px)',
                  background: 'rgba(255,255,255,0.1)',
                  borderRadius: '16px',
                  boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
                  transition: 'transform 0.4s cubic-bezier(0.34, 1.4, 0.64, 1)',
                  transform: chartView === 'hg' ? 'translateX(4px)' : 'translateX(calc(100% + 4px))',
                  zIndex: 0
                }} />
                <button onClick={() => setChartView('hg')} className={`dock-tab ${chartView === 'hg' ? 'active' : ''}`} style={{ position: 'relative', zIndex: 1, background: 'transparent', border: 'none' }}>H.G.</button>
                <button onClick={() => setChartView('ho')} className={`dock-tab ${chartView === 'ho' ? 'active' : ''}`} style={{ position: 'relative', zIndex: 1, background: 'transparent', border: 'none' }}>H.O.</button>
              </div>"""

code = code.replace(old_dock, new_dock)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated H.G. toggle with sliding pill.")
