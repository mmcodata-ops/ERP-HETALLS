import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def replace_block(pattern, new_block):
    global css
    new_css, count = re.subn(pattern, new_block, css, flags=re.DOTALL)
    if count == 0:
        print(f"Warning: could not match pattern {pattern[:30]}")
    else:
        css = new_css

replace_block(r"\.breakdown-tabs\s*\{.*?\}", 
""".breakdown-tabs {
  display: inline-flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 50px !important;
  padding: 4px !important;
  gap: 2px;
  flex-wrap: wrap;
  margin: 12px 24px;
}""")

replace_block(r"\.breakdown-tab\s*\{.*?\}", 
""".breakdown-tab {
  background: transparent;
  color: #a1a1aa;
  border: 1px solid transparent;
  border-radius: 50px;
  padding: 6px 14px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}""")

replace_block(r"\.breakdown-tab:hover\s*\{.*?\}", 
""".breakdown-tab:hover {
  color: #ffffff;
}""")

replace_block(r"\.breakdown-tab\.active\s*\{.*?\}", 
""".breakdown-tab.active {
  background: rgba(255, 255, 255, 0.08) !important;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
}""")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Breakdown tabs matched to Redflap")
