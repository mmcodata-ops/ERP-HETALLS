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

replace_block(r"\.kpi-grid\s*\{.*?\}", 
""".kpi-grid {
  display: flex;
  background: rgba(255, 255, 255, 0.02) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 30px !important;
  padding: 6px !important;
  gap: 4px;
  margin-bottom: 24px;
  align-items: stretch;
}""")

replace_block(r"\.kpi-card:hover\s*\{.*?\}", 
""".kpi-card:hover {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
  transform: translateY(-2px);
}""")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("KPI grid styles matched to Redflap")
