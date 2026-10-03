import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find {old[:40].replace(chr(10), ' ')}")
    css = css.replace(old, new, count)

# 1. Update Body for a gorgeous Aurora/Mesh background
old_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #050a15;
  background-image: 
    radial-gradient(circle at 15% 50%, rgba(14, 165, 233, 0.18) 0%, transparent 50%),
    radial-gradient(circle at 85% 30%, rgba(16, 185, 129, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 50% 100%, rgba(59, 130, 246, 0.15) 0%, transparent 60%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""

new_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #020617;
  background-image: 
    radial-gradient(circle at 0% 0%, rgba(56, 189, 248, 0.25) 0%, transparent 50%),
    radial-gradient(circle at 100% 0%, rgba(139, 92, 246, 0.25) 0%, transparent 40%),
    radial-gradient(circle at 100% 100%, rgba(236, 72, 153, 0.2) 0%, transparent 50%),
    radial-gradient(circle at 0% 100%, rgba(16, 185, 129, 0.15) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.15) 0%, transparent 60%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}"""
safe_replace(old_body, new_body)

# 2. Update .kpi-card to stunning bevel glass
old_kpi = """.kpi-card {
  background: rgba(20, 30, 45, 0.35) !important;
  backdrop-filter: blur(28px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(200%) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 16px !important;
  padding: 16px !important;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.2), inset 0 1px 1px rgba(255,255,255,0.2) !important;
}"""

new_kpi = """.kpi-card {
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
}
.kpi-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 45px rgba(0,0,0,0.35), inset 0 2px 2px rgba(255,255,255,0.2) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
}"""
safe_replace(old_kpi, new_kpi)


# 3. Update .card (charts)
old_card = """.card {
  background: rgba(20, 30, 45, 0.35) !important;
  backdrop-filter: blur(28px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(200%) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 20px !important;
  padding: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.2) !important;
}"""

new_card = """.card {
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
safe_replace(old_card, new_card)

# 4. Update the sidebar
old_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: rgba(10, 20, 35, 0.4) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.3) !important;
  display: flex;"""

new_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: linear-gradient(to right, rgba(0,0,0,0.6) 0%, rgba(255,255,255,0.02) 100%) !important;
  backdrop-filter: blur(40px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 5px 0 45px rgba(0, 0, 0, 0.4) !important;
  display: flex;"""
safe_replace(old_sidebar, new_sidebar)

# 5. Update header
old_header = """.header {
  height: var(--header-height);
  background: rgba(10, 20, 35, 0.3) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3) !important;
  display: flex; align-items: center; justify-content: space-between;"""

new_header = """.header {
  height: var(--header-height);
  background: linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(30px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3) !important;
  display: flex; align-items: center; justify-content: space-between;"""
safe_replace(old_header, new_header)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("UI enhancements applied")
