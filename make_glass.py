import os

file_path = 'frontend/src/pages/Forecast.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add ChevronDown to imports
content = content.replace(
    "TrendingUp, Target, Activity, CheckCircle, Clock, AlertTriangle, AlertCircle, DollarSign",
    "TrendingUp, Target, Activity, CheckCircle, Clock, AlertTriangle, AlertCircle, DollarSign, ChevronDown"
)

# 2. Add isDropdownOpen state
content = content.replace(
    "const [selectedPortal, setSelectedPortal] = useState('All')",
    "const [selectedPortal, setSelectedPortal] = useState('All')\n  const [isDropdownOpen, setIsDropdownOpen] = useState(false)"
)

# 3. Replace the <select> with the custom GlassDropdown
target_select = """            <select 
              value={selectedPortal} 
              onChange={(e) => setSelectedPortal(e.target.value)} 
              style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid var(--border-color)', color: '#fff', borderRadius: '4px', padding: '6px 12px', outline: 'none', cursor: 'pointer', fontSize: '13px' }}
            >
              <option value="All">All Channels</option>
              {portalData.map(p => <option key={p.name} value={p.name}>{p.name}</option>)}
            </select>"""

glass_dropdown = """            <div style={{ position: 'relative' }}>
              <div 
                onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                style={{ 
                  background: 'rgba(255,255,255,0.05)', 
                  backdropFilter: 'blur(10px)', WebkitBackdropFilter: 'blur(10px)',
                  border: '1px solid rgba(255,255,255,0.15)', 
                  color: '#fff', 
                  borderRadius: '6px', 
                  padding: '6px 12px', 
                  cursor: 'pointer', 
                  fontSize: '13px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
                }}
              >
                {selectedPortal === 'All' ? 'All Channels' : selectedPortal}
                <ChevronDown size={14} />
              </div>
              
              {isDropdownOpen && (
                <div style={{
                  position: 'absolute',
                  top: '100%',
                  right: 0,
                  marginTop: '8px',
                  width: '220px',
                  background: 'rgba(15, 23, 42, 0.75)',
                  backdropFilter: 'blur(16px)', WebkitBackdropFilter: 'blur(16px)',
                  border: '1px solid rgba(255,255,255,0.15)',
                  borderRadius: '8px',
                  boxShadow: '0 10px 40px rgba(0,0,0,0.5)',
                  zIndex: 50,
                  overflow: 'hidden'
                }}>
                  <div 
                    onClick={() => { setSelectedPortal('All'); setIsDropdownOpen(false) }}
                    style={{ padding: '10px 16px', fontSize: '13px', cursor: 'pointer', background: selectedPortal === 'All' ? 'rgba(59,130,246,0.4)' : 'transparent', borderBottom: '1px solid rgba(255,255,255,0.05)', transition: 'background 0.2s' }}
                    onMouseEnter={(e) => e.currentTarget.style.background = 'rgba(255,255,255,0.1)'}
                    onMouseLeave={(e) => e.currentTarget.style.background = selectedPortal === 'All' ? 'rgba(59,130,246,0.4)' : 'transparent'}
                  >
                    All Channels
                  </div>
                  <div style={{ maxHeight: '250px', overflowY: 'auto' }}>
                    {portalData.map(p => (
                      <div 
                        key={p.name}
                        onClick={() => { setSelectedPortal(p.name); setIsDropdownOpen(false) }}
                        style={{ padding: '10px 16px', fontSize: '13px', cursor: 'pointer', background: selectedPortal === p.name ? 'rgba(59,130,246,0.4)' : 'transparent', transition: 'background 0.2s' }}
                        onMouseEnter={(e) => e.currentTarget.style.background = 'rgba(255,255,255,0.1)'}
                        onMouseLeave={(e) => e.currentTarget.style.background = selectedPortal === p.name ? 'rgba(59,130,246,0.4)' : 'transparent'}
                      >
                        {p.name}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>"""

content = content.replace(target_select, glass_dropdown)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Liquid glass dropdown created")
