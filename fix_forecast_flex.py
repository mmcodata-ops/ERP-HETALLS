import os

file_path = 'frontend/src/pages/Forecast.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "<div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '24px', marginBottom: '24px' }}>",
    "<div style={{ display: 'flex', flexWrap: 'wrap', gap: '24px', marginBottom: '24px' }}>"
)
content = content.replace(
    '<div className="card" style={{ padding: \'24px\' }}>',
    '<div className="card" style={{ padding: \'24px\', flex: \'1 1 300px\' }}>'
)
content = content.replace(
    '<div className="card" style={{ padding: \'24px\', height: \'320px\', gridColumn: \'span 2\' }}>',
    '<div className="card" style={{ padding: \'24px\', height: \'320px\', flex: \'2 1 500px\' }}>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Flexbox layout fixed.")
