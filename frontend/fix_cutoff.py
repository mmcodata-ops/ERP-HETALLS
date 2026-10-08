import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix desktop main-content layout to prevent right-side cutoff
new_main_content = """.main-content {
  margin-left: calc(var(--sidebar-width) + 24px);
  width: calc(100vw - var(--sidebar-width) - 24px);
  max-width: calc(100vw - var(--sidebar-width) - 24px);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}"""

css = re.sub(r"\.main-content\s*\{[\s\S]*?flex-direction: column;\s*\}", new_main_content, css, count=1)

# Ensure mobile view uses 100vw correctly without overflowing
new_mobile_main = """.main-content {
      margin-left: 0 !important;
      width: 100vw !important;
      max-width: 100vw !important;
      box-sizing: border-box;
    }"""
css = re.sub(r"\.main-content\s*\{\s*margin-left: 0 !important;[\s\S]*?max-width: 100vw !important;\s*\}", new_mobile_main, css)

# Make sure .page-body uses box-sizing: border-box so padding doesn't add to width
css = css.replace(".page-body {\n    padding: 28px 32px;\n    flex: 1;\n  }", ".page-body {\n    padding: 28px 32px;\n    flex: 1;\n    box-sizing: border-box;\n  }")

# Check if box-sizing is global, if not, add it to *
if "*, *::before, *::after" not in css:
    css = "*, *::before, *::after { box-sizing: border-box; }\n" + css

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed desktop and mobile right-edge cutoff issue.")
