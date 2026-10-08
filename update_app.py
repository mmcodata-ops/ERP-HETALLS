import os

file_path = 'frontend/src/App.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'import Forecast from' not in content:
    content = content.replace("import Dashboard from './pages/Dashboard'", "import Dashboard from './pages/Dashboard'\nimport Forecast from './pages/Forecast'")
    content = content.replace('<Route path="/dashboard" element={<Dashboard />} />', '<Route path="/dashboard" element={<Dashboard />} />\n            <Route path="/forecast" element={<Forecast />} />')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("App.jsx updated")
else:
    print("Already updated")
