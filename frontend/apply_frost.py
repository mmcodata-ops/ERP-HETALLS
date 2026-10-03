import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

frost_bg = "linear-gradient(110deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.05) 35%, rgba(255,255,255,0.01) 100%)"
frost_blur = "blur(16px) saturate(120%)"
frost_shadow = "0 10px 30px rgba(0, 0, 0, 0.2), inset 1px 1px 3px rgba(255, 255, 255, 0.4)"

# KPI Card
old_kpi = """.kpi-card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 36px !important;
  padding: 24px 20px !important;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3), inset 0 2px 5px rgba(255, 255, 255, 0.15) !important;
}"""
new_kpi = f""".kpi-card {{
  background: {frost_bg} !important;
  backdrop-filter: {frost_blur} !important;
  -webkit-backdrop-filter: {frost_blur} !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 20px !important;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: {frost_shadow} !important;
}}"""
safe_replace(old_kpi, new_kpi)

# Card
old_card = """.card {
  background: rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 32px !important;
  padding: 24px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3), inset 0 2px 5px rgba(255, 255, 255, 0.1) !important;
}"""
new_card = f""".card {{
  background: {frost_bg} !important;
  backdrop-filter: {frost_blur} !important;
  -webkit-backdrop-filter: {frost_blur} !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 24px;
  box-shadow: {frost_shadow} !important;
}}"""
safe_replace(old_card, new_card)

# Login
old_login = """.login-card {
  background: rgba(255, 255, 255, 0.06) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 40px !important;
  padding: 48px 44px;
  width: 420px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3), inset 0 2px 5px rgba(255, 255, 255, 0.15) !important;
  position: relative; z-index: 1;
}"""
new_login = f""".login-card {{
  background: {frost_bg} !important;
  backdrop-filter: {frost_blur} !important;
  -webkit-backdrop-filter: {frost_blur} !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 48px 44px;
  width: 420px;
  box-shadow: {frost_shadow} !important;
  position: relative; z-index: 1;
}}"""
safe_replace(old_login, new_login)

# Table
old_table = """.breakdown-table-wrapper {
  overflow: auto;
  background: rgba(255, 255, 255, 0.04) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 24px !important;
  flex: 1;
  min-height: 0;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3), inset 0 2px 5px rgba(255, 255, 255, 0.1) !important;
}"""
new_table = f""".breakdown-table-wrapper {{
  overflow: auto;
  background: {frost_bg} !important;
  backdrop-filter: {frost_blur} !important;
  -webkit-backdrop-filter: {frost_blur} !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  flex: 1;
  min-height: 0;
  box-shadow: {frost_shadow} !important;
}}"""
safe_replace(old_table, new_table)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied frost glass styles!")
