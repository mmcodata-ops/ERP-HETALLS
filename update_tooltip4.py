import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_tooltip = """const ProgressChartTooltip = ({ active, payload, label, data, chartView, chartGroupBy }) => {
  const [isClosed, setIsClosed] = useState(false);

  useEffect(() => {
    setIsClosed(false);
  }, [label]);

  if (isClosed || !active || !payload || !payload.length) return null;

  const portalItems = payload.filter(p => p.dataKey !== 'order_count_hg' && p.dataKey !== 'order_count_ho' && p.dataKey !== 'month' && p.dataKey !== '_dt')
  const salesCountItem = payload.find(p => p.dataKey === (chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'))
  const currentIndex = data.findIndex(d => d.month === label)
  const previousDataRaw = currentIndex > 0 ? data[currentIndex - 1] : null
  const isCurrentPeriod = currentIndex === data.length - 1
  const previousData = previousDataRaw

  // ALWAYS show all portals with non-zero values
  const filteredItems = [...portalItems].filter(p => Number(p.value));

  const total = filteredItems.reduce((sum, item) => sum + (Number(item.value) || 0), 0)

  // Label Generation
  const day = new Date().getDate();
  const currLabel = (chartGroupBy === 'mtd' || isCurrentPeriod) ? `(1-${day})` : "(Full Month)";
  const prevLabel = (chartGroupBy === 'mtd') ? `(1-${day})` : "(Full Month)";
  const currentMonthName = label ? label.split(' ')[0] : '';
  const prevMonthName = previousData ? previousData.month.split(' ')[0] : '';

  const getPercentageStr = (prev, curr) => {
    if (prev > 0) {
      const pct = ((curr - prev) / prev) * 100
      const sign = pct > 0 ? "+" : ""
      const color = pct >= 0 ? "var(--success)" : "var(--danger)"
      return ` <span style={{color: '${color}', fontSize: '11px', marginLeft: '4px'}}>(${sign}${pct.toFixed(2)}%)</span>`
    } else if (curr > 0 && prev === 0) {
      return ` <span style={{color: 'var(--success)', fontSize: '11px', marginLeft: '4px'}}>(+100.00%)</span>`
    }
    return ""
  }

  return (
    <div style={{
      background: '#0f172a', border: '1px solid var(--border)',
      borderRadius: '12px', padding: '12px 14px', fontSize: 13,
      boxShadow: 'var(--shadow), var(--glass-shine)',
      backdropFilter: 'blur(32px) saturate(200%)',
      WebkitBackdropFilter: 'blur(32px) saturate(200%)',
      minWidth: '240px'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12, borderBottom: '1px solid var(--border)', paddingBottom: 6 }}>
        <p style={{ color: 'var(--text-muted)', margin: 0, fontWeight: 'bold' }}>
          {chartGroupBy === 'mtd' ? 'Date View (Month-To-Date)' : 'Month View (Full Month)'}
        </p>
        <button 
          className="tooltip-close-btn"
          onClick={(e) => { e.stopPropagation(); setIsClosed(true); }}
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '2px', display: 'flex', alignItems: 'center' }}
        >
          <X size={16} />
        </button>
      </div>

      {filteredItems.map(item => {
        const prev = previousData ? (Number(previousData[item.dataKey]) || 0) : 0;
        const curr = Number(item.value) || 0;
        return (
          <div key={item.dataKey} style={{ marginBottom: 10 }}>
            <div style={{ color: item.color, fontWeight: 600 }}>{item.dataKey}:</div>
            <div style={{ display: 'flex', justifyContent: 'space-between', paddingLeft: 8, color: 'var(--text)', marginTop: 2 }}>
              <span>{currentMonthName} {currLabel}:</span>
              <span>${curr.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', paddingLeft: 8, color: 'var(--text-muted)', fontSize: '12px', marginTop: 1 }}>
              <span>{prevMonthName} {prevLabel}:</span>
              <span dangerouslySetInnerHTML={{__html: `$${prev.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}${getPercentageStr(prev, curr)}`}} />
            </div>
          </div>
        );
      })}

      <div style={{ marginTop: 10, paddingTop: 10, borderTop: '1px dashed var(--border)', fontWeight: 600 }}>
        <div style={{ color: 'var(--text)', marginBottom: 4 }}>TOTAL REVENUE:</div>
        <div style={{ display: 'flex', justifyContent: 'space-between', paddingLeft: 8 }}>
          <span>{currentMonthName} {currLabel}:</span>
          <span>${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</span>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', paddingLeft: 8, color: 'var(--text-muted)', fontSize: '12px', marginTop: 1 }}>
          <span>{prevMonthName} {prevLabel}:</span>
          <span dangerouslySetInnerHTML={{__html: `$${(previousData ? filteredItems.reduce((sum, item) => sum + (Number(previousData[item.dataKey]) || 0), 0) : 0).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}${getPercentageStr(previousData ? filteredItems.reduce((sum, item) => sum + (Number(previousData[item.dataKey]) || 0), 0) : 0, total)}`}} />
        </div>
      </div>

      {salesCountItem && (
        <div style={{ marginTop: 10, paddingTop: 10, borderTop: '1px dashed var(--border)', color: 'var(--danger)', fontWeight: 600 }}>
          <div style={{ marginBottom: 4 }}>SALES COUNT:</div>
          <div style={{ display: 'flex', justifyContent: 'space-between', paddingLeft: 8 }}>
            <span>{currentMonthName} {currLabel}:</span>
            <span>{salesCountItem.value}</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', paddingLeft: 8, color: 'var(--danger)', opacity: 0.8, fontSize: '12px', marginTop: 1 }}>
            <span>{prevMonthName} {prevLabel}:</span>
            <span dangerouslySetInnerHTML={{__html: `${previousData ? (Number(previousData[salesCountItem.dataKey]) || 0) : 0}${getPercentageStr(previousData ? (Number(previousData[salesCountItem.dataKey]) || 0) : 0, salesCountItem.value)}`}} />
          </div>
        </div>
      )}
    </div>
  )
}"""

start_idx = content.find("const ProgressChartTooltip =")
end_idx = content.find("export default function Dashboard() {")

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_tooltip + "\n\n" + content[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced ProgressChartTooltip.")
else:
    print("Could not find start or end index.")
