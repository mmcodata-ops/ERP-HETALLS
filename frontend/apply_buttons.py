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

# 1. Update .btn-primary to be a sleek pill glass button
replace_block(r"\.btn-primary\s*\{.*?\}",
""".btn-primary {
  width: 100%; padding: 14px 20px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px) saturate(120%);
  -webkit-backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-top: 1px solid rgba(255, 255, 255, 0.35);
  border-left: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff; font-size: 15px; font-weight: 600;
  border-radius: 50px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2);
  display: flex; align-items: center; justify-content: center; gap: 8px;
}""")
replace_block(r"\.btn-primary:hover\s*\{.*?\}",
""".btn-primary:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3), inset 0 1px 2px rgba(255, 255, 255, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.45);
}""")

# 2. Update .form-input to match the "How can I help?" box
replace_block(r"\.form-input\s*\{.*?\}",
""".form-input {
  width: 100%; padding: 14px 20px;
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  border-left: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 50px;
  color: #ffffff; font-size: 14px;
  transition: all 0.3s ease;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}""")
replace_block(r"\.form-input:focus\s*\{.*?\}",
""".form-input:focus {
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.05);
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.1), inset 0 2px 4px rgba(0, 0, 0, 0.2);
}""")

# 3. Update .company-bill-btn
replace_block(r"\.company-bill-btn\s*\{.*?\}",
""".company-bill-btn {
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(20px) saturate(120%);
  -webkit-backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  border-left: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff !important;
  font-weight: 600;
  padding: 14px 20px;
  border-radius: 50px;
  text-align: center;
  text-decoration: none;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}""")
replace_block(r"\.company-bill-btn:hover\s*\{.*?\}",
""".company-bill-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3), inset 0 1px 2px rgba(255, 255, 255, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.45);
}""")

# 4. Update breakdown tabs
replace_block(r"\.breakdown-tab\s*\{.*?\}",
""".breakdown-tab {
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 50px;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.05);
}""")
replace_block(r"\.breakdown-tab\.active\s*\{.*?\}",
""".breakdown-tab.active {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-top: 1px solid rgba(255, 255, 255, 0.4);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.3);
}""")
replace_block(r"\.breakdown-tab:hover\s*\{.*?\}",
""".breakdown-tab:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
}""")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied VisionOS pill button styles")
