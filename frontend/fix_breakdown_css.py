import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

custom_css = """
/* --- STATIC BREAKDOWN CARD HEIGHT FIX --- */
.breakdown-static-card,
.breakdown-static-card .kpi-card {
  min-height: 140px !important;
  height: 100% !important;
}

@media (max-width: 900px) {
  .breakdown-static-card,
  .breakdown-static-card .kpi-card {
    min-height: 115px !important;
  }
}
"""

if "STATIC BREAKDOWN CARD HEIGHT FIX" not in css:
    css += "\n" + custom_css
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added custom CSS for static breakdown card.")
else:
    print("CSS already present.")
