import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a global override at the very end of the file
global_override = """
/* --- OVERRIDE FOR HORIZONTAL SCROLL DOCK --- */
.kpi-grid {
  display: flex !important;
  flex-wrap: nowrap !important;
  overflow-x: auto !important;
  overflow-y: hidden !important;
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}
.kpi-grid::-webkit-scrollbar {
  display: none !important;
}
.kpi-grid > * {
  flex: 0 0 calc(20% - 5px) !important;
  min-width: 250px !important;
  max-width: calc(20% - 5px) !important;
}
@media (max-width: 1400px) {
  .kpi-grid > * {
    flex: 0 0 250px !important;
    max-width: 250px !important;
  }
}
"""

if "/* --- OVERRIDE FOR HORIZONTAL SCROLL DOCK --- */" not in css:
    css += "\n" + global_override

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added global override for horizontal scroll dock.")
