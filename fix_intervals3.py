import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the main fetchAll interval
content = content.replace('const interval = setInterval(() => fetchAll(false), 5000);', '')
content = content.replace('clearInterval(interval);', '')

# 2. Fix the breakdown interval block
old_bd = '''  useEffect(() => {
    let interval;
    if (showBreakdown) {
      interval = setInterval(() => {
        let url = bdTab;
        if (bdTab === 'custom') {
          url = bdCustomDate;
          if (bdCustomEndDate) url += |;
        }
        axios.get(${API}/api/breakdown/daily-sales?date=&_=)
          .then(res => setBdData(res.data))
          .catch(console.error);
      }, 15000); // Poll every 15 seconds
    }
    return () => clearInterval(interval);
  }, [showBreakdown, bdTab, bdCustomDate, bdCustomEndDate, API])'''

new_bd = '''  // Removed auto-refresh intervals per user request
  useEffect(() => {}, [showBreakdown, bdTab, bdCustomDate, bdCustomEndDate, API])'''

content = content.replace(old_bd, new_bd)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
