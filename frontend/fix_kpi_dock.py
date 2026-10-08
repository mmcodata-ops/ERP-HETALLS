import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous override to match the "Dock" style (1 row of 6 on desktop)
# and exactly 1 column on mobile screens.

override_css = """
/* --- KPI GRID SPACING OVERRIDES --- */
.kpi-grid {
  display: flex !important;
  flex-direction: row !important;
  gap: 12px !important;
  padding: 12px !important;
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 32px !important;
  align-items: stretch !important;
  overflow-x: hidden;
}

/* Ensure all 6 cards fit evenly on large screens */
.kpi-grid > * {
  flex: 1 1 0 !important;
  min-width: 0 !important;
  width: auto !important;
}

/* Tablet / Small Desktop View: fallback to 3x2 grid if screen gets too narrow for 6 inline */
@media (max-width: 1250px) {
  .kpi-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 16px !important;
    padding: 16px !important;
    border-radius: 28px !important;
  }
}

/* Medium Tablet View: 2 columns */
@media (max-width: 900px) {
  .kpi-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 16px !important;
  }
}

/* Mobile View: EXACTLY ONE CARD PER ROW AS REQUESTED */
@media (max-width: 600px) {
  .kpi-grid {
    grid-template-columns: repeat(1, 1fr) !important;
    gap: 12px !important;
    padding: 12px !important;
    border-radius: 20px !important;
  }
}

.kpi-card, .cube-container {
  margin: 0 !important;
}
"""

# Replace the old override block
css = re.sub(r'/\* --- KPI GRID SPACING OVERRIDES --- \*/[\s\S]*?(?=$)', '', css)
css += override_css

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated KPI grid to single row dock on desktop and 1 card per row on mobile.")
