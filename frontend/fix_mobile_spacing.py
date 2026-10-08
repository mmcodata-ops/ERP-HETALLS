import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a clean header definition for mobile to ensure it has margin from the edges
mobile_header_css = """
  .header {
    padding: 0 16px !important;
    margin: 16px !important;
    width: calc(100% - 32px) !important;
    border-radius: 20px !important;
  }
"""

# We'll just inject it safely at the end of the mobile media query
css = css.replace("/* --- SIDEBAR MOBILE FIXES --- */", "/* --- SIDEBAR MOBILE FIXES --- */\n@media (max-width: 900px) {" + mobile_header_css + "}")

# Also ensure page-body on mobile has better padding
css = css.replace("padding: 16px !important;", "padding: 16px 20px !important;")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed mobile header and body spacing.")
