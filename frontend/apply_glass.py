import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(pattern, replacement):
    global css
    new_css, count = re.subn(pattern, replacement, css, flags=re.DOTALL)
    if count == 0:
        print(f"Warning: could not replace pattern {pattern[:30]}...")
    else:
        css = new_css

# 1. KPI Card
safe_replace(
    r'\.kpi-card \{.*?box-shadow:.*?;.*?\}',
    '''.kpi-card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: var(--radius);
  padding: 20px;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
}'''
)

# 2. Card
safe_replace(
    r'\.card \{.*?box-shadow:.*?;.*?\}',
    '''.card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
}'''
)

# 3. Login Card
safe_replace(
    r'\.login-card \{.*?z-index: 1;.*?\}',
    '''.login-card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(24px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 20px;
  padding: 48px 44px;
  width: 420px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
  position: relative; z-index: 1;
}'''
)

# 4. Table wrapper
safe_replace(
    r'\.breakdown-table-wrapper \{.*?min-height: 0;.*?\}',
    '''.breakdown-table-wrapper {
  overflow: auto;
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 8px;
  flex: 1;
  min-height: 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
}'''
)

# 5. Sidebar
safe_replace(
    r'\.sidebar \{.*?box-shadow:.*?;.*?\}',
    '''.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: rgba(255, 255, 255, 0.02) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.4) !important;
  display: flex;
}'''
)

# 6. Header
safe_replace(
    r'\.header \{.*?z-index: 50;.*?\}',
    '''.header {
  height: var(--header-height);
  background: rgba(255, 255, 255, 0.02) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4) !important;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 0; z-index: 50;
}'''
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Glass theme applied without touching colors")
