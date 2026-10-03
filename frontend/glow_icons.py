import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find {old[:40]}")
    css = css.replace(old, new, count)

old_gold = ".kpi-icon.gold, .kpi-icon.warning { background: rgba(245,158,11,0.15); color: var(--gold); }"
new_gold = ".kpi-icon.gold, .kpi-icon.warning { background: rgba(245,158,11,0.15); color: var(--gold); box-shadow: 0 0 15px rgba(245,158,11,0.3); border: 1px solid rgba(245,158,11,0.3); }"
safe_replace(old_gold, new_gold)

old_green = ".kpi-icon.green, .kpi-icon.success { background: rgba(16,185,129,0.15); color: var(--success); }"
new_green = ".kpi-icon.green, .kpi-icon.success { background: rgba(16,185,129,0.15); color: var(--success); box-shadow: 0 0 15px rgba(16,185,129,0.3); border: 1px solid rgba(16,185,129,0.3); }"
safe_replace(old_green, new_green)

old_red = ".kpi-icon.red, .kpi-icon.danger { background: rgba(239,68,68,0.15);  color: var(--danger); }"
new_red = ".kpi-icon.red, .kpi-icon.danger { background: rgba(239,68,68,0.15); color: var(--danger); box-shadow: 0 0 15px rgba(239,68,68,0.3); border: 1px solid rgba(239,68,68,0.3); }"
safe_replace(old_red, new_red)

old_blue = ".kpi-icon.blue, .kpi-icon.info { background: rgba(59,130,246,0.15); color: var(--info); }"
new_blue = ".kpi-icon.blue, .kpi-icon.info { background: rgba(59,130,246,0.15); color: var(--info); box-shadow: 0 0 15px rgba(59,130,246,0.3); border: 1px solid rgba(59,130,246,0.3); }"
safe_replace(old_blue, new_blue)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Icon glows added")
