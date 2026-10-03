import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new):
    global css
    if old not in css:
        print(f"Warning: could not find exact match for \n{old[:80]}...\n")
    css = css.replace(old, new, 1)

# Sidebar Nav Items
old_nav = """.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 12px;
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 14px; font-weight: 500;
  transition: all var(--transition);
  margin-bottom: 2px;
  cursor: pointer;
}"""
new_nav = """.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 16px;
  border-radius: 50px;
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-secondary);
  font-size: 14px; font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  margin-bottom: 4px;
  cursor: pointer;
}"""
safe_replace(old_nav, new_nav)

old_nav_hover = """.nav-item:hover { background: var(--bg-hover); color: var(--text-primary); }"""
new_nav_hover = """.nav-item:hover { 
  background: rgba(255, 255, 255, 0.03); 
  border: 1px solid rgba(255, 255, 255, 0.1); 
  color: #ffffff; 
}"""
safe_replace(old_nav_hover, new_nav_hover)

old_nav_active = """.nav-item.active {
  background: var(--gold-glow);
  color: var(--gold);
  border: 1px solid var(--border-accent);
}"""
new_nav_active = """.nav-item.active {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-top: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.3);
}"""
safe_replace(old_nav_active, new_nav_active)

old_nav_svg = """.nav-item.active svg { color: var(--gold); }"""
new_nav_svg = """.nav-item.active svg { color: #ffffff; }"""
safe_replace(old_nav_svg, new_nav_svg)

# Breakdown / Chart Tabs (HG/HO)
old_tab_active = """.breakdown-tab.active {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-top: 1px solid rgba(255, 255, 255, 0.4);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.3);
}"""
new_tab_active = """.breakdown-tab.active {
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.5);
  color: #ffffff;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25), inset 0 1px 3px rgba(255, 255, 255, 0.4);
}"""
safe_replace(old_tab_active, new_tab_active)


with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated sidebar and buttons to visionos")
