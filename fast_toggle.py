import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. State changes
content = content.replace("const [revenueChart, setRevenueChart] = useState(null)", 
"""const [revenueChartMonth, setRevenueChartMonth] = useState(null)
  const [revenueChartMtd, setRevenueChartMtd] = useState(null)""")

# 2. fetchAll Promise changes
old_fetch = """        Promise.allSettled([
          axios.get(`${API}/api/dashboard/kpis?_t=${t}`),
          axios.get(`${API}/api/dashboard/revenue-chart?group_by=${chartGroupByRef.current}&_t=${t}`),
          axios.get(`${API}/api/dashboard/recent-orders?_t=${t}`),
          axios.get(`${API}/api/dashboard/today-orders?_t=${t}`),
          axios.get(`${API}/api/dashboard/companies-revenue?_t=${t}`),
        ]).then(([k, r, o, tData, c]) => {
          if (!isMounted) return;
          if (k.status === 'fulfilled') setKpis(k.value.data);
          if (r.status === 'fulfilled') setRevenueChart(r.value.data);"""

new_fetch = """        Promise.allSettled([
          axios.get(`${API}/api/dashboard/kpis?_t=${t}`),
          axios.get(`${API}/api/dashboard/revenue-chart?group_by=month&_t=${t}`),
          axios.get(`${API}/api/dashboard/revenue-chart?group_by=mtd&_t=${t}`),
          axios.get(`${API}/api/dashboard/recent-orders?_t=${t}`),
          axios.get(`${API}/api/dashboard/today-orders?_t=${t}`),
          axios.get(`${API}/api/dashboard/companies-revenue?_t=${t}`),
        ]).then(([k, rMonth, rMtd, o, tData, c]) => {
          if (!isMounted) return;
          if (k.status === 'fulfilled') setKpis(k.value.data);
          if (rMonth.status === 'fulfilled') setRevenueChartMonth(rMonth.value.data);
          if (rMtd.status === 'fulfilled') setRevenueChartMtd(rMtd.value.data);"""

content = content.replace(old_fetch, new_fetch)

# 3. Chart uses derived data
content = content.replace("data={revenueChart || []}", "data={(chartGroupBy === 'month' ? revenueChartMonth : revenueChartMtd) || []}")
content = content.replace("data={revenueChart}", "data={(chartGroupBy === 'month' ? revenueChartMonth : revenueChartMtd) || []}")
# (Handle the ternary one if it exists)
content = content.replace("data={fullScreenChart === 'hg' ? revenueChart : revenueChart}", "data={(chartGroupBy === 'month' ? revenueChartMonth : revenueChartMtd) || []}")

# 4. Button onClicks
old_btn = """<button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => {
                chartGroupByRef.current = 'month';
                setChartGroupBy('month');
                axios.get(`${API}/api/dashboard/revenue-chart?group_by=month&_t=${Date.now()}`).then(r => setRevenueChart(r.data));
              }}>Month</button>
              <button className={chartGroupBy === 'mtd' ? 'on' : ''} onClick={() => {
                chartGroupByRef.current = 'mtd';
                setChartGroupBy('mtd');
                axios.get(`${API}/api/dashboard/revenue-chart?group_by=mtd&_t=${Date.now()}`).then(r => setRevenueChart(r.data));
              }}>Date</button>"""

new_btn = """<button className={chartGroupBy === 'month' ? 'on' : ''} onClick={() => {
                chartGroupByRef.current = 'month';
                setChartGroupBy('month');
              }}>Month</button>
              <button className={chartGroupBy === 'mtd' ? 'on' : ''} onClick={() => {
                chartGroupByRef.current = 'mtd';
                setChartGroupBy('mtd');
              }}>Date</button>"""
content = content.replace(old_btn, new_btn)

# 5. Fix Tooltip spacing
old_tooltip_item = """<div key={i} className="tooltip-item" style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
            <span style={{ color: p.color, fontWeight: 600 }}>{p.name}:</span>
            <span style={{ color: 'var(--gold)', fontWeight: 'bold' }} dangerouslySetInnerHTML={{ __html: `$${Number(p.value).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}${percentageStr}` }} />
          </div>"""
new_tooltip_item = """<div key={i} className="tooltip-item" style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4, gap: '16px' }}>
            <span style={{ color: p.color, fontWeight: 600, whiteSpace: 'nowrap' }}>{p.name}:</span>
            <span style={{ color: 'var(--gold)', fontWeight: 'bold', whiteSpace: 'nowrap', textAlign: 'right' }} dangerouslySetInnerHTML={{ __html: `$${Number(p.value).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}${percentageStr}` }} />
          </div>"""
content = content.replace(old_tooltip_item, new_tooltip_item)

# Also fix the tooltip overall width or title padding
old_tooltip_total = """<div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 8, paddingTop: 8, borderTop: '1px dashed var(--border)', fontWeight: 600 }}>"""
new_tooltip_total = """<div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 8, paddingTop: 8, borderTop: '1px dashed var(--border)', fontWeight: 600, gap: '16px' }}>"""
content = content.replace(old_tooltip_total, new_tooltip_total)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
