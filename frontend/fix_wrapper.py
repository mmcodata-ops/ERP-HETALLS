import sys
with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find {old[:40]}")
    css = css.replace(old, new, count)

old_table = """.breakdown-table-wrapper {
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
new_table = """.breakdown-table-wrapper {
  overflow: auto;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.0) 100%) !important;
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  flex: 1;
  min-height: 0;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5), inset 0 2px 10px rgba(255,255,255,0.1) !important;
}"""
safe_replace(old_table, new_table)
with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
