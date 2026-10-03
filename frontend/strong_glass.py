import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

# 1. Update .kpi-card to STRONGER glass
old_kpi = """.kpi-card {
  background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(40px) saturate(250%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(250%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 20px !important;
  padding: 20px 18px !important;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative; overflow: hidden;
  box-shadow: 0 15px 35px rgba(0,0,0,0.25), inset 0 2px 2px rgba(255,255,255,0.1) !important;
}"""

new_kpi = """.kpi-card {
  background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.02) 100%) !important;
  backdrop-filter: blur(24px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.4) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-radius: 20px !important;
  padding: 20px 18px !important;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative; overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.4), inset 0 2px 10px rgba(255,255,255,0.25) !important;
}"""
safe_replace(old_kpi, new_kpi)

# Update hover for kpi
old_kpi_hover = """.kpi-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 45px rgba(0,0,0,0.35), inset 0 2px 2px rgba(255,255,255,0.2) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
}"""
new_kpi_hover = """.kpi-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 50px rgba(0,0,0,0.5), inset 0 2px 15px rgba(255,255,255,0.35) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.5) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.35) !important;
}"""
safe_replace(old_kpi_hover, new_kpi_hover)

# 2. Update .card to STRONGER glass
old_card = """.card {
  background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(40px) saturate(250%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(250%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 24px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3), inset 0 1px 1px rgba(255,255,255,0.1) !important;
}"""

new_card = """.card {
  background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.02) 100%) !important;
  backdrop-filter: blur(24px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.35) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 24px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4), inset 0 2px 10px rgba(255,255,255,0.2) !important;
}"""
safe_replace(old_card, new_card)

# 3. Table wrapper strong glass
old_table = """.breakdown-table-wrapper {
  overflow: auto;
  border: 1px solid var(--border);
  border-radius: 20px;
  background: rgba(20, 30, 45, 0.25) !important;
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  flex: 1;
  min-height: 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
}"""

new_table = """.breakdown-table-wrapper {
  overflow: auto;
  border-top: 1px solid rgba(255, 255, 255, 0.35) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.02) 100%) !important;
  backdrop-filter: blur(24px) saturate(200%);
  -webkit-backdrop-filter: blur(24px) saturate(200%);
  flex: 1;
  min-height: 0;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4), inset 0 2px 10px rgba(255,255,255,0.2) !important;
}"""
safe_replace(old_table, new_table)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Strong glass effect applied")
