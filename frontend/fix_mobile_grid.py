import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

fix_css = """

/* --- BULLETPROOF MOBILE GRID FIX --- */
@media (max-width: 900px) {
  .kpi-grid {
    display: grid !important;
    width: 100% !important;
    box-sizing: border-box !important;
    justify-content: stretch !important;
    align-content: stretch !important;
  }
  .kpi-grid > * {
    width: 100% !important;
    max-width: 100% !important;
    justify-self: stretch !important;
    margin: 0 !important;
  }
  .cube-container, .breakdown-static-card {
    width: 100% !important;
    box-sizing: border-box !important;
  }
}
"""

if "/* --- BULLETPROOF MOBILE GRID FIX --- */" not in css:
    css += fix_css
    
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Added mobile grid stretch fix")
