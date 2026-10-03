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
        print("Matched and replaced successfully.")

# Update dock-container to match Redflap track precisely
replace_block(r"\.dock-container\s*\{.*?\}", 
""".dock-container {
  display: inline-flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 50px !important;
  padding: 4px !important;
  gap: 2px;
}""")

# Update dock-tab to match Redflap items precisely
replace_block(r"\.dock-tab\s*\{.*?\}",
""".dock-tab {
  background: transparent;
  color: #a1a1aa;
  border: 1px solid transparent;
  border-radius: 50px;
  padding: 6px 14px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
}""")

# Update dock-tab:hover
replace_block(r"\.dock-tab:hover\s*\{.*?\}",
""".dock-tab:hover {
  color: #ffffff;
}""")

# Update dock-tab.active to match Redflap active state
replace_block(r"\.dock-tab\.active\s*\{.*?\}",
""".dock-tab.active {
  background: rgba(255, 255, 255, 0.08) !important;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
}""")


with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Redflap dock styles applied.")
