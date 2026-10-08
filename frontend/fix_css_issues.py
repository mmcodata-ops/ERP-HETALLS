import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix scrollbar corner
if "::-webkit-scrollbar-corner" not in css:
    css = css.replace("::-webkit-scrollbar-thumb:hover { background: var(--gold-dark); }",
                      "::-webkit-scrollbar-thumb:hover { background: var(--gold-dark); }\n::-webkit-scrollbar-corner { background: transparent !important; }")

# 2. Fix sticky first column for the breakdown table
sticky_css = """
/* Sticky First Column for Breakdown Table */
.breakdown-table td:first-child,
.breakdown-table th:first-child {
  position: sticky !important;
  left: 0;
  z-index: 10;
  background: var(--bg-surface) !important;
}
.breakdown-table thead th:first-child {
  z-index: 30 !important;
  background: #0f172a !important;
}
"""
if "Sticky First Column for Breakdown Table" not in css:
    css += "\n" + sticky_css

# 3. Fix .breakdown-tabs to be a horizontally scrollable ribbon instead of wrapping multi-line pill
old_tabs_css = """.breakdown-tabs {
  display: inline-flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 50px !important;
  padding: 4px !important;
  gap: 2px;
  flex-wrap: wrap;
  margin: 12px 24px;
}"""

new_tabs_css = """.breakdown-tabs {
  display: flex !important;
  align-items: center;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 12px !important;
  padding: 6px 12px !important;
  gap: 8px;
  flex-wrap: nowrap !important;
  overflow-x: auto !important;
  overflow-y: hidden !important;
  white-space: nowrap !important;
  margin: 12px 24px;
  max-width: calc(100% - 48px);
}
.breakdown-tabs::-webkit-scrollbar { display: none; }
"""

if old_tabs_css in css:
    css = css.replace(old_tabs_css, new_tabs_css)
else:
    # try regex replacement for the breakdown-tabs
    tabs_regex = r"\.breakdown-tabs\s*\{[^}]+\}"
    if re.search(tabs_regex, css):
        # Only replace the first occurrence (desktop), the mobile one can just inherit or be overridden
        css = re.sub(tabs_regex, new_tabs_css, css, count=1)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS fixes applied successfully.")
