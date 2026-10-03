import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

pattern = r"\.breakdown-tabs\s*\{.*?\.breakdown-tab\.active\s*\{.*?\}\s*"

new_tabs = """.breakdown-tabs {
  display: flex;
  background: rgba(10, 15, 30, 0.4) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 50px !important;
  padding: 6px !important;
  gap: 4px;
  align-items: center;
  flex-wrap: wrap;
  margin: 12px 24px;
}
.breakdown-tab {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid transparent;
  border-radius: 50px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.breakdown-tab:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.03);
}
.breakdown-tab.active {
  background: rgba(255, 255, 255, 0.1) !important;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.4) !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2) !important;
}
"""

css, count = re.subn(pattern, new_tabs, css, flags=re.DOTALL)
if count > 0:
    print("Replaced breakdown tabs successfully.")
else:
    print("Could not find breakdown tabs pattern.")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
