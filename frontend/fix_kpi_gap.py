import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace all explicit gap values inside .kpi-grid declarations
def replace_gap(match):
    # If inside a media query, we might want different gaps. We'll do a global replace first, 
    # then fix the media queries.
    return match.group(0)

# The most robust way is to just append an override at the very end of the CSS file.
# Since the user specifically wants more gap between KPI cards on desktop AND mobile.

override_css = """

/* --- KPI GRID SPACING OVERRIDES --- */
.kpi-grid {
  gap: 24px !important;
  padding: 16px !important;
}

@media (max-width: 1100px) {
  .kpi-grid {
    gap: 16px !important;
    padding: 16px !important;
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
  }
}

@media (max-width: 900px) {
  .kpi-grid {
    gap: 16px !important;
    padding: 16px !important;
  }
}

@media (max-width: 600px) {
  .kpi-grid {
    gap: 12px !important;
    padding: 12px !important;
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

/* Ensure the cards themselves don't overlap the grid borders */
.kpi-card, .cube-container {
  margin: 0 !important;
}
"""

css += override_css

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added explicit gap overrides for KPI grid.")
