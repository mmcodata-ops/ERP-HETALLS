import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

old_kpi = """.kpi-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: var(--shadow), var(--glass-shine);
}"""
new_kpi = """.kpi-card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(24px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: var(--radius);
  padding: 20px;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
}"""
safe_replace(old_kpi, new_kpi)

old_card = """.card {
  background: #0b1120 !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), var(--glass-shine);
}"""
new_card = """.card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(24px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
}"""
safe_replace(old_card, new_card)

old_login = """.login-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 48px 44px;
  width: 420px;
  box-shadow: var(--shadow);
  position: relative; z-index: 1;
}"""
new_login = """.login-card {
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(24px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 20px;
  padding: 48px 44px;
  width: 420px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
  position: relative; z-index: 1;
}"""
safe_replace(old_login, new_login)

old_table = """.breakdown-table-wrapper {
  overflow: auto;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-card);
  flex: 1;
  min-height: 0;
}"""
new_table = """.breakdown-table-wrapper {
  overflow: auto;
  background: rgba(255, 255, 255, 0.03) !important;
  backdrop-filter: blur(24px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 8px;
  flex: 1;
  min-height: 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
}"""
safe_replace(old_table, new_table)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Safely replaced CSS")
