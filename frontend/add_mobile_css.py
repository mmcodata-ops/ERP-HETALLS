import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

responsive_css = """
/* --- MOBILE RESPONSIVENESS OVERRIDES --- */
@media (max-width: 1100px) {
  .kpi-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    border-radius: 24px !important;
    gap: 8px !important;
  }
  .kpi-grid > *:first-child {
    grid-column: auto !important;
  }
  .kpi-card {
    padding: 16px !important;
  }
}

@media (max-width: 768px) {
  .kpi-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    border-radius: 20px !important;
  }
  .kpi-grid > *:first-child {
    grid-column: auto !important;
  }
}

@media (max-width: 480px) {
  .kpi-grid {
    grid-template-columns: 1fr !important;
    border-radius: 16px !important;
  }
  .kpi-grid > *:first-child {
    grid-column: auto !important;
  }
}
"""

css = re.sub(r"/\* --- MOBILE RESPONSIVENESS OVERRIDES --- \*/.*", responsive_css, css, flags=re.DOTALL)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated mobile overrides to ensure no accidental spanning.")
