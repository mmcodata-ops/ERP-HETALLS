import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace the bulletproof mobile grid fix with a cleaner grid-auto-rows solution
grid_regex = re.compile(r'/\* --- BULLETPROOF MOBILE GRID FIX ---\s*\*/.*?@media \(max-width: 900px\) \{.*?(?=\/\* --- STATIC BREAKDOWN CARD HEIGHT FIX --- \*\/)', re.DOTALL)

new_grid_css = """/* --- BULLETPROOF MOBILE GRID FIX --- */
  @media (max-width: 900px) {
    .kpi-grid {
      display: grid !important;
      grid-auto-rows: 1fr !important;
      width: 100% !important;
      box-sizing: border-box !important;
      justify-content: stretch !important;
      align-content: stretch !important;
    }
    .kpi-grid > * {
      width: auto !important;
      max-width: none !important;
      justify-self: stretch !important;
      align-self: stretch !important;
      margin: 0 !important;
      height: 100% !important;
    }
    .cube-container, .breakdown-static-card {
      width: 100% !important;
      height: 100% !important;
      box-sizing: border-box !important;
      min-height: 0 !important;
    }
    .cube, .cube-face {
      min-height: 0 !important;
      height: 100% !important;
      max-height: none !important;
    }
    .breakdown-static-card .kpi-card {
      height: 100% !important;
      min-height: 0 !important;
      max-height: none !important;
    }
  }
  
  """

css = grid_regex.sub(new_grid_css, css)

# 2. Add mobile header centering and gap fix
header_mobile_css = """
  /* --- MOBILE HEADER CENTERING & GAP FIX --- */
  @media (max-width: 900px) {
    .header {
      position: relative !important;
      border-radius: 16px !important;
      margin: 12px 16px 8px 16px !important;
      width: calc(100% - 32px) !important;
      display: flex !important;
      align-items: center !important;
    }
    .header-left {
      position: absolute !important;
      left: 50% !important;
      transform: translateX(-50%) !important;
      width: max-content !important;
      text-align: center !important;
      justify-content: center !important;
    }
    .page-body {
      padding: 4px 16px 16px 16px !important;
    }
    .kpi-grid {
      margin-bottom: 16px !important;
    }
  }
"""

if "/* --- MOBILE HEADER CENTERING & GAP FIX --- */" not in css:
    css += header_mobile_css

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated index.css with perfect grid sizes and centered header")
