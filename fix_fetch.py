import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix fetchAll
old_block = """        Promise.allSettled([
          axios.get(`${API}/api/dashboard/kpis?_t=${t}`),
          axios.get(`${API}/api/dashboard/revenue-chart?group_by=${chartGroupByRef.current}&_t=${t}`),
          axios.get(`${API}/api/dashboard/recent-orders?_t=${t}`),
          axios.get(`${API}/api/dashboard/today-orders?_t=${t}`),
          axios.get(`${API}/api/dashboard/companies-revenue?_t=${t}`),
        ]).then(([k, r, o, tData, c]) => {
          if (!isMounted) return;
          if (k.status === 'fulfilled') setKpis(k.value.data);
          if (r.status === 'fulfilled') setRevenueChart(r.value.data);"""

new_block = """        Promise.allSettled([
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

content = content.replace(old_block, new_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
