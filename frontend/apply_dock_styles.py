import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new):
    global css
    if old not in css:
        print(f"Warning: could not find exact match for \n{old[:80]}...\n")
    css = css.replace(old, new, 1)

# 1. Add dock styles
dock_styles = """
/* "?"?"? Dock Styles (Redflap-like) "?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"?"? */
.dock-container {
  display: flex;
  background: rgba(10, 15, 30, 0.4) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 50px !important;
  padding: 6px !important;
  gap: 4px;
}
.dock-tab {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid transparent;
  border-radius: 50px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.dock-tab:hover {
  color: #ffffff;
}
.dock-tab.active {
  background: rgba(255, 255, 255, 0.1) !important;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.4) !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2) !important;
}

"""

if "Dock Styles" not in css:
    css += dock_styles

# 2. Update KPI Grid and Card
old_kpi_grid = """.kpi-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}"""
new_kpi_grid = """.kpi-grid {
  display: flex;
  background: rgba(10, 15, 30, 0.4) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 30px !important;
  padding: 8px !important;
  gap: 4px;
  margin-bottom: 24px;
  align-items: stretch;
}"""
safe_replace(old_kpi_grid, new_kpi_grid)

css = re.sub(r"\.kpi-card\s*\{.*?\}", 
""".kpi-card {
  background: transparent !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border-radius: 24px !important;
  border: 1px solid transparent !important;
  box-shadow: none !important;
  padding: 16px 20px !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative; overflow: hidden;
  flex: 1;
  min-width: 0;
}""", css, flags=re.DOTALL)

# Add active/hover state to KPI card simulating dock tab
css = re.sub(r"\.kpi-card:hover\s*\{.*?\}", 
""".kpi-card:hover {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2) !important;
  transform: translateY(-2px);
}""", css, flags=re.DOTALL)


# 3. Update Sidebar to look like a dock
css = re.sub(r"\.sidebar\s*\{.*?\}", 
""".sidebar {
  background: rgba(10, 15, 30, 0.4) !important;
  backdrop-filter: blur(16px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(150%) !important;
  border-radius: 30px !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4), inset 0 1px 2px rgba(255, 255, 255, 0.1) !important;

  position: fixed;
  top: 16px; left: 16px;
  width: var(--sidebar-width);
  height: calc(100vh - 32px);
  
  display: flex;
  flex-direction: column;
  z-index: 100;
  overflow-y: auto;
}""", css, count=1, flags=re.DOTALL)

# 4. Update main-content margin
old_main = """.main-content {
  flex: 1;
  margin-left: var(--sidebar-width);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}"""
new_main = """.main-content {
  flex: 1;
  margin-left: calc(var(--sidebar-width) + 24px);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}"""
safe_replace(old_main, new_main)

# 5. Fix Header spacing
old_header = """height: var(--header-height);
  
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 0; z-index: 50;"""
new_header = """height: var(--header-height);
  
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 16px; z-index: 50;
  margin-right: 16px;
  border-radius: 30px !important;"""
safe_replace(old_header, new_header)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated CSS with Redflap dock styles")
