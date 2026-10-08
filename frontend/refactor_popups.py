import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """            style={{
              position: 'absolute', top: '105%', left: '50%', transform: 'translateX(-50%)', minWidth: '260px', zIndex: 9999,
              background: '#070b16', border: '1px solid var(--border-accent)', borderRadius: '12px',
              padding: '14px', boxShadow: '0 20px 50px rgba(0, 0, 0, 0.8), var(--glass-shine)',
            }}"""

replacement = """            className="card-detail-popup" """

content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard.jsx updated")
