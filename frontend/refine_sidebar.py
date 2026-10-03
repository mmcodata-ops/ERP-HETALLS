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

replace_block(r"\.sidebar\s*\{.*?\}", 
""".sidebar {
  background: rgba(255, 255, 255, 0.02) !important;
  backdrop-filter: blur(16px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(150%) !important;
  border-radius: 24px !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4) !important;

  position: fixed;
  top: 16px; left: 16px;
  width: var(--sidebar-width);
  height: calc(100vh - 32px);
  
  display: flex;
  flex-direction: column;
  z-index: 100;
  overflow-y: auto;
}""")

replace_block(r"\.nav-item\s*\{.*?\}", 
""".nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 16px;
  border-radius: 50px;
  background: transparent;
  border: 1px solid transparent;
  color: #a1a1aa;
  font-size: 14px; font-weight: 500;
  transition: all 0.3s ease;
  margin-bottom: 4px;
  cursor: pointer;
}""")

replace_block(r"\.nav-item:hover\s*\{.*?\}", 
""".nav-item:hover { 
  color: #ffffff; 
}""")

replace_block(r"\.nav-item\.active\s*\{.*?\}", 
""".nav-item.active {
  background: rgba(255, 255, 255, 0.08) !important;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
}""")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Sidebar styles matched to Redflap")
