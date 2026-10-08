import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add BreakdownStaticCard component
card_comp = """
const BreakdownStaticCard = ({ style = {}, openBreakdown }) => {
  const [isHovered, setIsHovered] = useState(false);
  
  return (
    <div 
      key="breakdown" 
      onClick={openBreakdown} 
      className="breakdown-static-card" 
      style={{ cursor: 'pointer', display: 'flex', flexDirection: 'column', flex: 1, position: 'relative', zIndex: isHovered ? 9999 : 1, ...style }}
      onMouseEnter={() => { if (window.matchMedia('(hover: hover)').matches) setIsHovered(true); }}
      onMouseLeave={() => { if (window.matchMedia('(hover: hover)').matches) setIsHovered(false); }}
    >
      <KPICard icon={Layers} label="Detailed Breakdown" value="Breakdown" sub="Daily Sale Brands & Portal" colorClass="blue" format="text" />
      
      {isHovered && (
        <div 
          onClick={(e) => e.stopPropagation()}
          style={{
            position: 'absolute', top: '105%', left: '50%', transform: 'translateX(-50%)', minWidth: '260px', zIndex: 9999,
            background: '#070b16', border: '1px solid var(--border-accent)', borderRadius: '12px',
            padding: '14px', boxShadow: '0 20px 50px rgba(0, 0, 0, 0.8), var(--glass-shine)',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px', borderBottom: '1px solid var(--border)', paddingBottom: '8px' }}>
            <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--gold)' }}>
              Detailed Breakdown
            </span>
          </div>
          <div style={{ color: 'var(--text-primary)', fontSize: '12px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <span style={{ color: 'var(--text-muted)' }}>Click to view the daily sales report, brands, and portal data table.</span>
          </div>
        </div>
      )}
    </div>
  );
};
"""

if "const BreakdownStaticCard" not in code:
    code = code.replace("const PortalGrowthCard", card_comp + "\nconst PortalGrowthCard")

# 2. Replace inline Detailed Breakdown with BreakdownStaticCard
old_inline = """    <div key="breakdown" onClick={openBreakdown} className="breakdown-static-card" style={{ cursor: 'pointer', display: 'flex', flexDirection: 'column', flex: 1 }}>
      <KPICard icon={Layers} label="Detailed Breakdown" value="Breakdown" sub="Daily Sale Brands & Portal" colorClass="blue" format="text" />
    </div>"""

if old_inline in code:
    code = code.replace(old_inline, '      <BreakdownStaticCard key="breakdown" openBreakdown={openBreakdown} />,')
else:
    # Try regex
    inline_regex = r'<div key="breakdown"[^>]*className="breakdown-static-card"[^>]*>[\s\S]*?<KPICard[^>]*/>[\s\S]*?</div>'
    if re.search(inline_regex, code):
        code = re.sub(inline_regex, '      <BreakdownStaticCard key="breakdown" openBreakdown={openBreakdown} />', code)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Added BreakdownStaticCard with tooltip.")
