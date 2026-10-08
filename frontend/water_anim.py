import sys

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    if old_str not in code:
        print(f"WARNING: Could not find target in {filepath}")
        return False
    code = code.replace(old_str, new_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    return True

# 1. Fix sidebar sliding pill — add glow + smoother water-like curve
replace_in_file(
    'frontend/src/components/Sidebar.jsx',
    'style={{ position: "absolute", left: 12, right: 12, top: pillStyle.top, height: pillStyle.height, opacity: pillStyle.opacity, background: "rgba(255, 255, 255, 0.1)", borderRadius: "50px", transition: "all 0.45s cubic-bezier(0.22, 1, 0.36, 1)", zIndex: 0 }}',
    'style={{ position: "absolute", left: 8, right: 8, top: pillStyle.top, height: pillStyle.height, opacity: pillStyle.opacity, background: "linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04))", border: "1px solid rgba(255,255,255,0.1)", borderRadius: "14px", boxShadow: "0 0 20px rgba(255,255,255,0.03), inset 0 1px 0 rgba(255,255,255,0.1)", transition: "top 0.5s cubic-bezier(0.4, 0, 0, 1), height 0.5s cubic-bezier(0.4, 0, 0, 1), opacity 0.3s ease", zIndex: 0 }}'
)

# 2. Fix H.G./H.O. sliding pill — add glow + smoother water-like curve
replace_in_file(
    'frontend/src/pages/Dashboard.jsx',
    """<div style={{
                  position: 'absolute',
                  top: 4, bottom: 4, width: 'calc(50% - 4px)',
                  background: 'rgba(255,255,255,0.1)',
                  borderRadius: '16px',
                  boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
                  transition: 'transform 0.45s cubic-bezier(0.22, 1, 0.36, 1)',
                  transform: chartView === 'hg' ? 'translateX(4px)' : 'translateX(calc(100% + 4px))',
                  zIndex: 0
                }} />""",
    """<div style={{
                  position: 'absolute',
                  top: 3, bottom: 3, width: 'calc(50% - 4px)',
                  background: 'linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.04))',
                  borderRadius: '14px',
                  border: '1px solid rgba(255,255,255,0.08)',
                  boxShadow: '0 4px 16px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.15)',
                  transition: 'transform 0.5s cubic-bezier(0.4, 0, 0, 1)',
                  transform: chartView === 'hg' ? 'translateX(3px)' : 'translateX(calc(100% + 5px))',
                  zIndex: 0
                }} />"""
)

print("Applied water-smooth animation to both pills.")
