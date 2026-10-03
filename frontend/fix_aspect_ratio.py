import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_kpi_grid = r"\.kpi-grid\s*\{[^}]+\}"
new_kpi_grid = """.kpi-grid {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  overflow-y: hidden;
  scrollbar-width: none;
  -ms-overflow-style: none;
  
  background: rgba(10, 15, 30, 0.6) !important;
  border: 1px solid rgba(255, 255, 255, 0.06) !important;
  border-radius: 28px !important;
  padding: 6px !important;
  gap: 6px;
  margin-bottom: 24px;
}
.kpi-grid::-webkit-scrollbar {
  display: none;
}
"""
css = re.sub(old_kpi_grid, new_kpi_grid, css, count=1)

old_first_child_grid = r"\.kpi-grid\s*>\s*\*:first-child\s*\{[^}]+\}"
new_first_child_grid = """.kpi-grid > *:first-child {
  /* removed grid-column override so flex works */
}"""
if re.search(old_first_child_grid, css):
    css = re.sub(old_first_child_grid, new_first_child_grid, css)


# Now fix the grid children to have a fixed width to match the aspect ratio of 5 cards
# Currently it is:
# .kpi-grid > * {
#   height: 115px !important;
#   min-height: 115px !important;
#   max-height: 115px !important;
#   width: 100% !important;
#   display: flex;
#   flex-direction: column;
# }

old_child = r"\.kpi-grid\s*>\s*\*\s*\{[^}]+\}"
new_child = """.kpi-grid > * {
  height: 115px !important;
  min-height: 115px !important;
  max-height: 115px !important;
  flex: 0 0 calc(20% - 5px); /* Exactly 5 cards visible, maintaining the perfect length/width */
  min-width: 235px; /* Ensures they never squish on smaller screens, allowing scroll */
  display: flex;
  flex-direction: column;
}"""
css = re.sub(old_child, new_child, css, count=1)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated KPI grid to horizontal scrolling flex to maintain perfect aspect ratio.")
