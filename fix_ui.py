import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update ProgressChartTooltip back to compact layout
new_tooltip = """const ProgressChartTooltip = ({ active, payload, label, data, chartView, chartGroupBy }) => {
  const [isClosed, setIsClosed] = useState(false);

  useEffect(() => {
    setIsClosed(false);
  }, [label]);

  if (isClosed || !active || !payload || !payload.length) return null;

  const portalItems = payload.filter(p => p.dataKey !== 'order_count_hg' && p.dataKey !== 'order_count_ho' && p.dataKey !== 'month' && p.dataKey !== '_dt')
  const salesCountItem = payload.find(p => p.dataKey === (chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'))
  const currentIndex = data.findIndex(d => d.month === label)
  const previousData = currentIndex > 0 ? data[currentIndex - 1] : null

  // ALWAYS show all portals with non-zero values
  const filteredItems = [...portalItems].filter(p => Number(p.value));
  const total = filteredItems.reduce((sum, item) => sum + (Number(item.value) || 0), 0)

  const getPercentageStr = (prev, curr) => {
    if (prev > 0) {
      const pct = ((curr - prev) / prev) * 100
      const sign = pct > 0 ? "+" : ""
      const color = pct >= 0 ? "var(--success)" : "var(--danger)"
      return ` <span style="color:${color}; font-size:11px; margin-left:4px">(${sign}${pct.toFixed(2)}%)</span>`
    } else if (curr > 0 && prev === 0) {
      return ` <span style="color:var(--success); font-size:11px; margin-left:4px">(+100.00%)</span>`
    }
    return ""
  }

  return (
    <div style={{
      background: '#0f172a', border: '1px solid var(--border)',
      borderRadius: '12px', padding: '12px 14px', fontSize: 13,
      boxShadow: 'var(--shadow), var(--glass-shine)',
      backdropFilter: 'blur(32px) saturate(200%)',
      WebkitBackdropFilter: 'blur(32px) saturate(200%)'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
        <p style={{ color: 'var(--text-muted)', margin: 0 }}>
          {label}
        </p>
        <button 
          className="tooltip-close-btn"
          onClick={(e) => { e.stopPropagation(); setIsClosed(true); }}
          onTouchEnd={(e) => { e.preventDefault(); e.stopPropagation(); setIsClosed(true); }}
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '4px', display: 'flex', alignItems: 'center', touchAction: 'manipulation' }}
        >
          ✕
        </button>
      </div>
      {filteredItems.sort((a, b) => a.name.localeCompare(b.name)).map((p, i) => {
        let percentageStr = ""
        if (previousData) {
          percentageStr = getPercentageStr(Number(previousData[p.dataKey]) || 0, Number(p.value) || 0)
        }
        return (
          <div key={i} className="tooltip-item" style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
            <span style={{ color: p.color, fontWeight: 600 }}>{p.name}:</span>
            <span style={{ color: 'var(--gold)', fontWeight: 'bold' }} dangerouslySetInnerHTML={{ __html: `$${Number(p.value).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}${percentageStr}` }} />
          </div>
        )
      })}
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 8, paddingTop: 8, borderTop: '1px dashed var(--border)', fontWeight: 600 }}>
        <span style={{ color: 'var(--text)' }}>Total:</span>
        <span style={{ color: 'var(--text)' }} dangerouslySetInnerHTML={{ __html: `$${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}${previousData ? getPercentageStr(filteredItems.reduce((sum, item) => sum + (Number(previousData[item.dataKey]) || 0), 0), total) : ''}` }} />
      </div>
      {salesCountItem && (
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 4, paddingTop: 4, borderTop: '1px dashed var(--border)', color: 'var(--danger)', fontWeight: 600 }}>
          <span>Sales Count:</span>
          <span dangerouslySetInnerHTML={{ __html: `${salesCountItem.value}${previousData ? getPercentageStr(Number(previousData[salesCountItem.dataKey]) || 0, salesCountItem.value) : ''}` }} />
        </div>
      )}
    </div>
  )
}"""

match = re.search(r'const ProgressChartTooltip.*?return \(.*?</div>\n  \)\n}', content, re.DOTALL)
if match:
    content = content.replace(match.group(0), new_tooltip)
else:
    print("Could not replace tooltip")

# 2. Add chartGroupByRef
content = content.replace("const [chartGroupBy, setChartGroupBy] = useState('month')", "const [chartGroupBy, setChartGroupBy] = useState('month')\n  const chartGroupByRef = useRef('month')")

# 3. Replace fetchAll logic to use ref and update useEffect
content = content.replace("axios.get(`${API}/api/dashboard/revenue-chart?group_by=${chartGroupBy}&_t=${t}`)", "axios.get(`${API}/api/dashboard/revenue-chart?group_by=${chartGroupByRef.current}&_t=${t}`)")
content = content.replace("}, [API, chartGroupBy]);", "}, [API]);")

# 4. Update the toggle buttons to do a seamless fetch
old_toggle = """<button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => setChartGroupBy('month')}>Month</button>
              <button className={chartGroupBy === 'mtd' ? 'on' : ''} onClick={() => setChartGroupBy('mtd')}>Date</button>"""
new_toggle = """<button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => {
                chartGroupByRef.current = 'month';
                setChartGroupBy('month');
                axios.get(`${API}/api/dashboard/revenue-chart?group_by=month&_t=${Date.now()}`).then(r => setRevenueChart(r.data));
              }}>Month</button>
              <button className={chartGroupBy === 'mtd' ? 'on' : ''} onClick={() => {
                chartGroupByRef.current = 'mtd';
                setChartGroupBy('mtd');
                axios.get(`${API}/api/dashboard/revenue-chart?group_by=mtd&_t=${Date.now()}`).then(r => setRevenueChart(r.data));
              }}>Date</button>"""
content = content.replace(old_toggle, new_toggle)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fixes")
