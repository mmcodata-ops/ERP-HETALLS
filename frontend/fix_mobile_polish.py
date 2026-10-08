import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Global Box-Sizing
if "box-sizing: border-box;" not in css[:500]:
    # Let's just insert it after the imports
    css = css.replace("@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');", 
                      "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');\n\n*, *::before, *::after { box-sizing: border-box; }")

# 2. Add Mobile Chart Legend Overrides & Breakdown Modal Overrides
mobile_overrides = """
/* --- MOBILE UI POLISH --- */
@media (max-width: 600px) {
  /* Fix Chart Legends wrapping issues */
  .recharts-legend-wrapper {
    max-width: 100% !important;
    padding: 0 10px !important;
  }
  .recharts-legend-item {
    font-size: 10px !important;
    margin-right: 8px !important;
    display: inline-flex !important;
    align-items: center !important;
    margin-bottom: 4px !important;
  }
  .recharts-legend-item svg {
    width: 8px !important;
    height: 8px !important;
    margin-right: 4px !important;
  }
  
  /* Fix Breakdown Modal filters and table */
  .breakdown-modal {
    padding: 16px 12px !important;
    width: 95vw !important;
  }
  .breakdown-tabs {
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    white-space: nowrap !important;
    border-radius: 12px !important;
    padding: 4px !important;
    width: 100% !important;
    -webkit-overflow-scrolling: touch;
  }
  .breakdown-tabs::-webkit-scrollbar {
    display: none;
  }
  .breakdown-tab, .breakdown-tab-custom {
    flex-shrink: 0 !important;
  }
  .breakdown-table-wrapper {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    width: 100% !important;
  }
  
  /* Give Dashboard a tiny bit more breathing room so the right edge isn't hitting scrollbars */
  .page-body {
    padding: 16px 16px !important;
  }
}
"""

if "/* --- MOBILE UI POLISH --- */" not in css:
    css += "\n" + mobile_overrides

# If .page-body doesn't have border-box explicitly, let's add it
if "box-sizing: border-box" not in css.split('.page-body {')[1].split('}')[0]:
    css = css.replace(".page-body {\n    padding: 28px 32px;\n    flex: 1;", ".page-body {\n    padding: 28px 32px;\n    flex: 1;\n    box-sizing: border-box;")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied global box-sizing, chart legend fixes, and mobile modal layout fixes.")
