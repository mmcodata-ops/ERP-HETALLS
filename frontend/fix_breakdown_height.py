import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the broken static card height fix
broken_css = """  /* --- STATIC BREAKDOWN CARD HEIGHT FIX --- */
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
  }"""

fixed_css = """  /* --- STATIC BREAKDOWN CARD HEIGHT FIX --- */
  .breakdown-static-card {
    min-height: 140px !important;
    display: flex !important;
    flex-direction: column !important;
    align-self: stretch !important;
    height: auto !important; /* Let grid/flex stretch it */
  }
  .breakdown-static-card .kpi-card {
    min-height: 140px !important;
    flex: 1 1 auto !important;
    height: auto !important;
  }
  
  @media (max-width: 900px) {
    .breakdown-static-card {
      min-height: 115px !important;
    }
    .breakdown-static-card .kpi-card {
      min-height: 115px !important;
    }
  }"""

if "height: 100% !important;" in broken_css and broken_css in css:
    css = css.replace(broken_css, fixed_css)
else:
    # Fallback if exact match fails
    css += "\n" + fixed_css

# Also fix the right gap globally for grid items
if "/* --- BULLETPROOF MOBILE GRID FIX --- */" in css:
    css = css.replace(
        "justify-self: stretch !important;",
        "justify-self: stretch !important;\n      align-self: stretch !important;"
    )

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated breakdown static card css")
