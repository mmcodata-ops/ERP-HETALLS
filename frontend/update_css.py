import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous .recharts-tooltip-wrapper override with .mobile-fixed-tooltip
target = """  /* Make Recharts tooltips fixed on mobile so they don't cover the bars when clicked */
  .recharts-tooltip-wrapper {
    position: fixed !important;
    top: 80px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    transition: none !important;
    z-index: 10000 !important;
    width: max-content;
  }"""

replacement = """  /* Make SPECIFIC Bar chart tooltips absolute inside the card on mobile */
  .mobile-fixed-tooltip {
    position: absolute !important;
    top: 60px !important; /* Touch the upper side of the bars */
    left: 50% !important;
    transform: translateX(-50%) !important;
    transition: none !important;
    z-index: 10000 !important;
    width: max-content;
    pointer-events: auto !important; /* To click the close button */
  }"""

css = css.replace(target, replacement)

# Add pointer-events to custom-tooltip to allow clicking X inside it
if 'pointer-events: auto' not in css and 'pointer-events' not in css.split('.custom-tooltip {')[1].split('}')[0]:
    css = css.replace('.custom-tooltip {', '.custom-tooltip {\n    pointer-events: auto;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated")
