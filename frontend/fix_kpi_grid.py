import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous override with a better one that forces 3x2 grid on desktop
override_css = """

/* --- KPI GRID SPACING OVERRIDES --- */
.kpi-grid {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 24px !important;
  padding: 20px !important;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 28px !important;
}

@media (max-width: 1200px) {
  .kpi-grid {
    gap: 20px !important;
    padding: 16px !important;
  }
}

@media (max-width: 900px) {
  .kpi-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    padding: 16px !important;
  }
}

@media (max-width: 600px) {
  .kpi-grid {
    grid-template-columns: repeat(1, 1fr) !important;
    gap: 12px !important;
    padding: 12px !important;
  }
}

/* Ensure the cards themselves don't overlap the grid borders */
.kpi-grid > * {
  flex: unset !important;
  width: 100% !important;
}
.kpi-card, .cube-container {
  margin: 0 !important;
}
"""

# replace the previous KPI GRID SPACING OVERRIDES block
css = re.sub(r'/\* --- KPI GRID SPACING OVERRIDES --- \*/[\s\S]*?(?=$)', '', css)
css += override_css

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Forced 3x2 grid layout and added gaps.")
