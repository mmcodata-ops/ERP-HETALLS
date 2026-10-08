import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """    }}>
      <p style={{ color: 'var(--text-muted)', marginBottom: 6 }}>{label}</p>"""

replacement = """    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
        <p style={{ color: 'var(--text-muted)', margin: 0 }}>{label}</p>
        <button 
          className="tooltip-close-btn"
          onClick={(e) => { e.stopPropagation(); setIsClosed(true); }}
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '2px', display: 'flex', alignItems: 'center' }}
        >
          <X size={16} />
        </button>
      </div>"""

new_content = content.replace(target, replacement)

if target in content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Close button successfully injected into ProgressChartTooltip")
else:
    print("Target not found. Please verify the code structure.")
