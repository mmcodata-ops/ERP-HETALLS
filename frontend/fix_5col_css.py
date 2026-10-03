import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the global override I added earlier
css = re.sub(r"/\* --- OVERRIDE FOR HORIZONTAL SCROLL DOCK --- \*/.*", "", css, flags=re.DOTALL)

# Re-define .kpi-grid and .kpi-card to perfectly match the 5-column mockup
old_kpi_grid = r"\.kpi-grid\s*\{[^}]+\}"
new_kpi_grid = """.kpi-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  background: rgba(14, 16, 25, 0.7) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 28px !important;
  padding: 8px !important;
  gap: 8px;
  margin-bottom: 24px;
}"""
css = re.sub(old_kpi_grid, new_kpi_grid, css, count=1)

old_kpi_card = r"\.kpi-card\s*\{[^}]+\}"
new_kpi_card = """.kpi-card {
  background: rgba(255, 255, 255, 0.02) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-radius: 20px !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  box-shadow: none !important;
  padding: 20px 24px !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative; overflow: hidden;
  min-width: 0;
}"""
css = re.sub(old_kpi_card, new_kpi_card, css, count=1)

# Ensure the active card has the glow
active_card_css = """.kpi-grid > *:first-child .kpi-card {
  background: linear-gradient(145deg, rgba(212, 175, 55, 0.15) 0%, rgba(212, 175, 55, 0.02) 100%) !important;
  border: 1px solid rgba(212, 175, 55, 0.3) !important;
  box-shadow: 0 0 20px rgba(212, 175, 55, 0.1), inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
}"""

old_active = r"\.kpi-grid\s*>\s*\*:first-child\s*\.kpi-card\s*\{[^}]+\}"
if re.search(old_active, css):
    css = re.sub(old_active, active_card_css, css)
else:
    css = css.replace(new_kpi_card, new_kpi_card + "\n" + active_card_css)

# Remove the explicit 115px height on .kpi-grid > * so they can size naturally
old_child = r"\.kpi-grid\s*>\s*\*\s*\{[^}]+\}"
new_child = """.kpi-grid > * {
  width: 100% !important;
  display: flex;
  flex-direction: column;
}"""
css = re.sub(old_child, new_child, css, count=1)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated KPI grid styles for perfect 5-column layout.")
