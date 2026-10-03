import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old}\n")
    css = css.replace(old, new, count)

old_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-base);
  background-image: 
    radial-gradient(at 0% 0%, rgba(79, 70, 229, 0.2) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.2) 0px, transparent 50%),
    radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.15) 0px, transparent 50%),
    radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.15) 0px, transparent 50%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""

new_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #030812;
  background-image: 
    radial-gradient(circle at 10% 20%, rgba(14, 165, 233, 0.15) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.1) 0%, transparent 60%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""
safe_replace(old_body, new_body)

old_root_radius = "--radius:        16px;"
new_root_radius = "--radius:        28px;"
safe_replace(old_root_radius, new_root_radius)

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
  background: var(--bg-card) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255,255,255,0.15);
}"""
safe_replace(old_card, new_card)

old_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: #060913 !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.7) !important;
}"""
new_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: rgba(10, 20, 35, 0.4) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.3) !important;
}"""
safe_replace(old_sidebar, new_sidebar)

old_header = """.header {
  height: var(--header-height);
  background: rgba(5, 8, 17, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 0; z-index: 10;
}"""
new_header = """.header {
  height: var(--header-height);
  background: rgba(10, 20, 35, 0.3) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 0; z-index: 10;
}"""
safe_replace(old_header, new_header)

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
  border: 1px solid var(--border);
  border-radius: 20px;
  background: rgba(20, 30, 45, 0.25) !important;
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  flex: 1;
  min-height: 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
}"""
safe_replace(old_table, new_table)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Safely replaced CSS blocks")
