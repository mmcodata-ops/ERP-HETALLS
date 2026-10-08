import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add state
if 'const [chartGroupBy, setChartGroupBy] = useState(\'month\')' not in content:
    content = content.replace("const [chartView, setChartView] = useState('hg')", "const [chartView, setChartView] = useState('hg')\n  const [chartGroupBy, setChartGroupBy] = useState('month')")

# Update fetchAll API call
target_api = "axios.get(`${API}/api/dashboard/revenue-chart?_t=${t}`)"
replacement_api = "axios.get(`${API}/api/dashboard/revenue-chart?group_by=${chartGroupBy}&_t=${t}`)"
content = content.replace(target_api, replacement_api)

# Update useEffect dependency
target_dep = "}, [API]);"
# Ensure we only replace the dependency array for the fetchAll useEffect
# The fetchAll useEffect starts with `let isMounted = true;`
target_useEffect = """      fetchAll(true);
      const interval = setInterval(() => fetchAll(false), 30000);
      return () => {
        isMounted = false;
        clearInterval(interval);
      };
    }, [API]);"""
replacement_useEffect = """      fetchAll(true);
      const interval = setInterval(() => fetchAll(false), 30000);
      return () => {
        isMounted = false;
        clearInterval(interval);
      };
    }, [API, chartGroupBy]);"""
content = content.replace(target_useEffect, replacement_useEffect)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard.jsx state and API fetch updated")
