import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix 1: Change kpi-grid to use grid
old_kpi_grid = """.kpi-grid {
  display: flex;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 30px !important;
  padding: 6px !important;
  gap: 4px;
  margin-bottom: 24px;
  align-items: stretch;
}"""

new_kpi_grid = """.kpi-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 30px !important;
  padding: 6px !important;
  gap: 4px;
  margin-bottom: 24px;
}"""
css = css.replace(old_kpi_grid, new_kpi_grid)

# Also fix the mobile media query kpi-grid
old_mobile_kpi = """.kpi-grid {
  display: flex;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 30px !important;
  padding: 6px !important;
  gap: 4px;
  margin-bottom: 24px;
  align-items: stretch;
}"""
# Wait, I already replaced it globally if it matches perfectly.
# Let's do it using regex to be safe.
css = re.sub(
    r"\.kpi-grid\s*\{\s*display:\s*flex;\s*background:\s*rgba\(255,\s*255,\s*255,\s*0\.02\)\s*!important;\s*border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.08\)\s*!important;\s*border-radius:\s*30px\s*!important;\s*padding:\s*6px\s*!important;\s*gap:\s*4px;\s*margin-bottom:\s*24px;\s*align-items:\s*stretch;\s*\}",
    new_kpi_grid,
    css
)

# Fix 2: Remove flex: 1 from .kpi-card
old_kpi_card = """.kpi-card {
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
}"""

new_kpi_card = """.kpi-card {
  background: transparent !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border-radius: 24px !important;
  border: 1px solid transparent !important;
  box-shadow: none !important;
  padding: 16px 20px !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative; overflow: hidden;
  min-width: 0;
}"""

if old_kpi_card in css:
    css = css.replace(old_kpi_card, new_kpi_card)
else:
    print("Could not exact match .kpi-card, trying regex...")
    css = re.sub(
        r"\.kpi-card\s*\{[^\}]+flex:\s*1;[^\}]+\}",
        lambda m: m.group(0).replace("flex: 1;", ""),
        css
    )

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Safely updated kpi-grid and kpi-card.")
