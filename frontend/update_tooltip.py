import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Modify ProgressChartTooltip
target = """const ProgressChartTooltip = ({ active, payload, label, data, chartView }) => {
  if (!active || !payload || !payload.length) return null"""

replacement = """const ProgressChartTooltip = ({ active, payload, label, data, chartView }) => {
  const [isClosed, setIsClosed] = useState(false);

  useEffect(() => {
    setIsClosed(false);
  }, [label]);

  if (isClosed || !active || !payload || !payload.length) return null;"""

content = content.replace(target, replacement)

# Add Close button to ProgressChartTooltip
target2 = """      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', borderBottom: '1px solid var(--border)', paddingBottom: '6px' }}>
        <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--text-muted)' }}>{label}</span>
      </div>"""

replacement2 = """      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', borderBottom: '1px solid var(--border)', paddingBottom: '6px' }}>
        <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--text-muted)' }}>{label}</span>
        <button 
          className="tooltip-close-btn"
          onClick={(e) => { e.stopPropagation(); setIsClosed(true); }}
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '2px', display: 'flex' }}
        >
          <X size={14} />
        </button>
      </div>"""

content = content.replace(target2, replacement2)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("ProgressChartTooltip updated")
