import os

file_path = 'frontend/src/pages/Forecast.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'const [isEditingTarget, setIsEditingTarget] = useState(false)',
    "const [isEditingTarget, setIsEditingTarget] = useState(false)\n  const [selectedPortal, setSelectedPortal] = useState('All')"
)
content = content.replace('Month End Sales Forecast', 'Site Preview')
content = content.replace(
    'Projecting month-end performance based on MTD sales.',
    'Projecting month-end performance for your sales channels.'
)

content = content.replace(
    'const mtdSales = portalData.reduce((acc, curr) => acc + curr.value, 0)',
    "const mtdSales = portalData.filter(p => selectedPortal === 'All' || p.name === selectedPortal).reduce((acc, curr) => acc + curr.value, 0)"
)
content = content.replace(
    'const portalStats = portalData.map(p => {',
    "const portalStats = portalData.filter(p => selectedPortal === 'All' || p.name === selectedPortal).map(p => {"
)

replacement_select = """          <select value={selectedPortal} onChange={(e) => setSelectedPortal(e.target.value)} style={{ background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border-color)', color: '#fff', borderRadius: '4px', padding: '6px 12px', outline: 'none' }}>
            <option value="All">All Sites</option>
            {portalData.map(p => <option key={p.name} value={p.name}>{p.name}</option>)}
          </select>
          <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
            Day {daysPassed} of {totalDays}
          </div>"""

target_div = """          <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
            Day {daysPassed} of {totalDays}
          </div>"""

content = content.replace(target_div, replacement_select)

# Fix the chart filtering so that it also filters by portal
chart_calc_target = """    if (dayData) {
      // Sum all portal sales for the day (excluding metadata keys)
      Object.keys(dayData).forEach(key => {
        if (!['month', 'order_count_hg', 'order_count_ho', '_dt'].includes(key)) {
          dayTotal += (dayData[key] || 0)
        }
      })
    }"""
    
chart_calc_replacement = """    if (dayData) {
      if (selectedPortal !== 'All') {
        // If a specific portal is selected, only add its sales for the day
        // We match by checking if the portal name (or something close) is in the keys
        // or just by exact match if possible.
        // Actually, daily data keys might be exactly portal names. Let's assume they are exact.
        if (dayData[selectedPortal]) {
           dayTotal += dayData[selectedPortal];
        } else {
           // Try to find the closest key (case insensitive or spaces)
           const pKey = Object.keys(dayData).find(k => k.toLowerCase() === selectedPortal.toLowerCase())
           if (pKey) dayTotal += dayData[pKey];
        }
      } else {
        // Sum all portal sales for the day (excluding metadata keys)
        Object.keys(dayData).forEach(key => {
          if (!['month', 'order_count_hg', 'order_count_ho', '_dt'].includes(key)) {
            dayTotal += (dayData[key] || 0)
          }
        })
      }
    }"""
    
content = content.replace(chart_calc_target, chart_calc_replacement)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Forecast.jsx updated to Site Preview with dropdown")
