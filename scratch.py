import re

with open("frontend/src/pages/Dashboard.jsx", "r", encoding="utf-8") as f:
    code = f.read()

hetalls_spinning_card = """
const HetallsSpinningCard = ({ companiesRev, isCurrency, style = {} }) => {
  const [spinCount, setSpinCount] = useState(0);
  const touchStartX = useRef(0);
  const [isHovered, setIsHovered] = useState(false);
  
  const getVal = (period) => {
    if (!companiesRev || !companiesRev[period]) return 0;
    return companiesRev[period].filter(c => c.name?.toUpperCase().includes('HETALLS')).reduce((s, c) => s + (isCurrency ? c.value : (c.order_count || 0)), 0) || 0;
  }
  
  const faces = [
    { 
      key: 'today', 
      label: isCurrency ? "HETALLS Revenue" : "HETALLS Orders", 
      value: getVal('today'), 
      sub: "Today only", 
      icon: isCurrency ? DollarSign : ShoppingCart, 
      colorClass: isCurrency ? 'purple' : 'pink' 
    },
    { 
      key: 'month', 
      label: isCurrency ? "HETALLS Month" : "HETALLS Month", 
      value: getVal('month'), 
      sub: "Month to date", 
      icon: isCurrency ? DollarSign : ShoppingCart, 
      colorClass: isCurrency ? 'purple' : 'pink' 
    },
    { 
      key: 'year', 
      label: isCurrency ? "HETALLS Year" : "HETALLS Year", 
      value: getVal('year'), 
      sub: isCurrency ? "Financial year" : "Year to date", 
      icon: isCurrency ? DollarSign : ShoppingCart, 
      colorClass: isCurrency ? 'purple' : 'pink' 
    },
  ];

  const getFace = (i) => {
    let k = spinCount - (spinCount % 3) + i;
    if (k < spinCount - 1) k += 3;
    return faces[k % faces.length];
  };

  const currentFace = faces[spinCount % 3];
  
  const currentItems = companiesRev ? companiesRev[currentFace.key]?.filter(c => c.name?.toUpperCase().includes('HETALLS')) : [];

  return (
    <div 
      style={{ position: 'relative', zIndex: isHovered ? 9999 : 1, ...style }}
      onMouseEnter={() => { if (window.matchMedia('(hover: hover)').matches) setIsHovered(true); }}
      onMouseLeave={() => { if (window.matchMedia('(hover: hover)').matches) setIsHovered(false); }}
    >
      <div 
        className="cube-container" 
        onClick={(e) => { 
          if (e && e.preventDefault) e.preventDefault(); 
          const rect = e.currentTarget.getBoundingClientRect();
          let clientX = e.clientX;
          if ((clientX === undefined || clientX === 0) && e.nativeEvent?.changedTouches?.length > 0) {
            clientX = e.nativeEvent.changedTouches[0].clientX;
          }
          const isRight = (clientX - rect.left) > rect.width / 2;
          setSpinCount(c => isRight ? c + 1 : (c - 1 + 300) % 300); 
          setIsHovered(true);
        }}
        onTouchStart={(e) => touchStartX.current = e.touches[0].clientX}
        onTouchEnd={(e) => {
          const diff = e.changedTouches[0].clientX - touchStartX.current;
          if (Math.abs(diff) > 30) {
            setSpinCount(c => diff > 0 ? (c - 1 + 300) % 300 : c + 1);
          }
        }}
        style={{ cursor: 'pointer', userSelect: 'none' }}
      >
        <div 
          className="cube" 
          style={{ 
            transform: `translateZ(-140px) rotateY(${spinCount * -120}deg)`, 
            transition: 'transform 0.4s ease-out' 
          }}
        >
          {[0, 1, 2].map(i => {
            const f = getFace(i);
            return (
              <div key={i} className="cube-face">
                <div style={{ width: '100%', height: '100%' }}>
                  <KPICard 
                    icon={f.icon} 
                    label={f.label} 
                    value={f.value} 
                    sub={f.sub} 
                    colorClass={f.colorClass} 
                    format={isCurrency ? "currency" : "number"}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {isHovered && currentItems && currentItems.length > 0 && (
        <div style={{
            position: 'absolute', top: '105%', left: 0, width: '100%', minWidth: '250px', zIndex: 9999,
            background: '#070b16', border: '1px solid var(--border-accent)', borderRadius: '12px',
            padding: '14px', boxShadow: '0 20px 50px rgba(0, 0, 0, 0.8), var(--glass-shine)',
          }}
          onClick={(e) => e.stopPropagation()}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px', borderBottom: '1px solid var(--border)', paddingBottom: '8px' }}>
            <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--gold)' }}>
              {currentFace.label} ({currentFace.key}):
            </span>
            <button 
              onClick={(e) => { e.stopPropagation(); setIsHovered(false); }}
              style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '2px 6px', fontSize: '14px', fontWeight: 'bold' }}
            >
              ✕
            </button>
          </div>
          <div style={{ maxHeight: '220px', overflowY: 'auto', paddingRight: '4px' }}>
            {currentItems.map((c, i) => (
              <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px', fontSize: '12px' }}>
                <span style={{ color: typeof getPortalColor !== 'undefined' ? getPortalColor(c.name, 0) : '#fff', fontWeight: 500 }}>{c.name}</span>
                <span style={{ fontWeight: 'bold', color: 'var(--text)' }}>
                   {isCurrency ? `$${Number(c.value).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}` : c.order_count}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
"""

# We also need to fix the CSS so the kpi-value isn't truncated!
# The user said: "first correct the this year revenue text that should be full text show"

# Let's replace the CSS.
css_file = "frontend/src/index.css"
with open(css_file, "r", encoding="utf-8") as f:
    css_code = f.read()
css_code = css_code.replace(".kpi-value  { font-size: 28px;", ".kpi-value  { font-size: 22px;")
with open(css_file, "w", encoding="utf-8") as f:
    f.write(css_code)

# Replace HetallsPopupCard with HetallsSpinningCard
pattern = re.compile(r'const HetallsPopupCard = \(\{.*?\}\)\s*=>\s*\{.*?\n\}\n', re.DOTALL)
new_code = pattern.sub(hetalls_spinning_card, code)

# Replace usage of HetallsPopupCard
usage_pattern = re.compile(r'<HetallsPopupCard key="htl-rev".*?/>', re.DOTALL)
new_code = usage_pattern.sub(r'<HetallsSpinningCard key="htl-rev" companiesRev={companiesRev} isCurrency={true} style={{ viewTransitionName: \'kpi-htl-rev\' }} />', new_code)

usage_pattern2 = re.compile(r'<HetallsPopupCard key="htl-ord".*?/>', re.DOTALL)
new_code = usage_pattern2.sub(r'<HetallsSpinningCard key="htl-ord" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: \'kpi-htl-ord\' }} />', new_code)

with open("frontend/src/pages/Dashboard.jsx", "w", encoding="utf-8") as f:
    f.write(new_code)

print("Done")
