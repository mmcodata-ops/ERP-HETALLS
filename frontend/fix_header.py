import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

pattern = r"\.header\s*\{.*?\s+height:\s*var\(--header-height\);\s+display:\s*flex;\s*align-items:\s*center;\s*justify-content:\s*space-between;\s+padding:\s*0\s+32px;\s+position:\s*sticky;\s*top:\s*0;\s*z-index:\s*50;\s*\}"

new_header = """.header {
  background: rgba(10, 15, 30, 0.4) !important;
  backdrop-filter: blur(12px) saturate(120%) !important;
  -webkit-backdrop-filter: blur(12px) saturate(120%) !important;
  border-radius: 30px !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.35) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.25) !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.15), inset 0 1px 2px rgba(255, 255, 255, 0.3) !important;

  height: var(--header-height);

  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 16px; z-index: 50;
  margin-right: 16px;
}"""

css, count = re.subn(pattern, new_header, css, flags=re.DOTALL)
if count > 0:
    print("Header fixed.")
else:
    print("Failed to replace header.")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

