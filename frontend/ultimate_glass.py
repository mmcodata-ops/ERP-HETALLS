import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:80]}...\n")
    css = css.replace(old, new, count)

# 1. Update Body to use a HIGH-RES LIQUID ABSTRACT IMAGE
old_body = """body {
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

new_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #050505;
  background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}
body::before {
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.5); /* Darkens the image so text is readable */
  z-index: -1;
}"""
safe_replace(old_body, new_body)

# 2. Refine KPI Card for true liquid glass (lower blur so background shapes show through)
old_kpi = """.kpi-card {
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

new_kpi = """.kpi-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.0) 100%) !important;
  backdrop-filter: blur(16px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 20px 18px !important;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative; overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 2px 10px rgba(255,255,255,0.15) !important;
}"""
safe_replace(old_kpi, new_kpi)

# 3. Refine Card (charts)
old_card = """.card {
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

new_card = """.card {
  background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.0) 100%) !important;
  backdrop-filter: blur(16px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-radius: 24px !important;
  padding: 24px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5), inset 0 2px 10px rgba(255,255,255,0.1) !important;
}"""
safe_replace(old_card, new_card)

# 4. Refine Sidebar
old_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: linear-gradient(to right, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(40px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
  box-shadow: 10px 0 45px rgba(0, 0, 0, 0.5) !important;
  display: flex;"""

new_sidebar = """.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: linear-gradient(to right, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.0) 100%) !important;
  backdrop-filter: blur(16px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 10px 0 45px rgba(0, 0, 0, 0.6) !important;
  display: flex;"""
safe_replace(old_sidebar, new_sidebar)

# 5. Refine Header
old_header = """.header {
  height: var(--header-height);
  background: linear-gradient(to bottom, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%) !important;
  backdrop-filter: blur(30px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
  display: flex; align-items: center; justify-content: space-between;"""

new_header = """.header {
  height: var(--header-height);
  background: linear-gradient(to bottom, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.0) 100%) !important;
  backdrop-filter: blur(16px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.15) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6) !important;
  display: flex; align-items: center; justify-content: space-between;"""
safe_replace(old_header, new_header)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("ULTIMATE Liquid glass background applied!")
