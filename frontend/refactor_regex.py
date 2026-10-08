import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"style=\{\{\s*position:\s*'absolute',\s*top:\s*'105%',\s*left:\s*'50%',\s*transform:\s*'translateX\(-50%\)',\s*minWidth:\s*'260px',\s*zIndex:\s*9999,\s*background:\s*'#070b16',\s*border:\s*'1px solid var\(--border-accent\)',\s*borderRadius:\s*'12px',\s*padding:\s*'14px',\s*boxShadow:\s*'0 20px 50px rgba\(0, 0, 0, 0\.8\), var\(--glass-shine\)',?\s*\}\}"

new_content, count = re.subn(pattern, 'className="card-detail-popup"', content)
print(f"Replaced {count} instances.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
