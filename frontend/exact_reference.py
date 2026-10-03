import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .kpi-grid
old_kpi_grid = r"\.kpi-grid\s*\{[^}]+\}"
new_kpi_grid = """.kpi-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  background: rgba(10, 15, 30, 0.6) !important;
  border: 1px solid rgba(255, 255, 255, 0.06) !important;
  border-radius: 28px !important;
  padding: 6px !important;
  gap: 6px;
  margin-bottom: 24px;
}"""
css = re.sub(old_kpi_grid, new_kpi_grid, css, count=1)

# Ensure mobile queries stay intact by not blindly replacing all. 
# Wait, I used count=1 so it only replaces the main one.

# Replace .kpi-card
old_kpi_card = r"\.kpi-card\s*\{[^}]+\}"
new_kpi_card = """.kpi-card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-radius: 22px !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  box-shadow: none !important;
  padding: 16px 20px !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative; overflow: hidden;
  min-width: 0;
}"""
css = re.sub(old_kpi_card, new_kpi_card, css, count=1)

# Add the active state for the first card
active_state = """
/* First card acts as the active tab */
.kpi-grid > *:first-child .kpi-card {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(245, 158, 11, 0.02) 100%) !important;
  border: 1px solid rgba(245, 158, 11, 0.25) !important;
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
}
"""

if "First card acts as the active tab" not in css:
    # insert it right after .kpi-card
    css = css.replace(new_kpi_card, new_kpi_card + "\n" + active_state)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied exact reference image style to KPI grid.")
