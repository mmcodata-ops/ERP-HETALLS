import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Update ProgressChartTooltip signature
content = content.replace('const ProgressChartTooltip = ({ active, payload, label, data }) => {',
                          'const ProgressChartTooltip = ({ active, payload, label, data, hoveredStack }) => {')

# Add filtering logic inside ProgressChartTooltip
filter_logic = '''      <p style={{ color: 'var(--text-muted)', marginBottom: 6 }}>{label}</p>
      {[...portalItems].filter(p => {
        if (!Number(p.value)) return false;
        if (hoveredStack === 'b') return p.name.includes('HETALLS');
        if (hoveredStack === 'a') return !p.name.includes('HETALLS');
        return true;
      }).sort((a, b) => a.name.localeCompare(b.name)).map((p, i) => {'''

content = content.replace('''      <p style={{ color: 'var(--text-muted)', marginBottom: 6 }}>{label}</p>
      {[...portalItems].filter(p => Number(p.value) > 0).sort((a, b) => a.name.localeCompare(b.name)).map((p, i) => {''', filter_logic)

# Wait, 	otal needs to be recalculated in the tooltip if filtered.
# Currently total is calculated earlier: const total = portalItems.reduce(...)
# Let's fix that calculation too.
