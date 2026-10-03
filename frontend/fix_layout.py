import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find \n{old[:50]}...\n")
    css = css.replace(old, new, count)

old_body = """body {
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

new_body = """body {
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
safe_replace(old_body, new_body)

old_kpi = """.kpi-card {
  background: rgba(20, 30, 45, 0.25) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  border-radius: var(--radius);
  padding: 20px;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 1px rgba(255,255,255,0.15) !important;
}"""
new_kpi = """.kpi-card {
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
safe_replace(old_kpi, new_kpi)

old_card = """.card {
  background: rgba(20, 30, 45, 0.25) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 32px;
  padding: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
}"""
new_card = """.card {
  background: rgba(20, 30, 45, 0.35) !important;
  backdrop-filter: blur(28px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(200%) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 20px !important;
  padding: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.2) !important;
}"""
safe_replace(old_card, new_card)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Layout fixes applied")
