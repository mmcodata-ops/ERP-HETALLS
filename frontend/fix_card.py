import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_card = """.card {
  background: var(--bg-card) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255,255,255,0.15);
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

if old_card in css:
    css = css.replace(old_card, new_card)
    print("Updated .card")

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
