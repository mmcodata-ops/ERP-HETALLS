import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new):
    global css
    if old not in css:
        print(f"Warning: could not find exact match for \n{old[:80]}...\n")
    css = css.replace(old, new, 1)

old_company = """.company-bill-btn {
  background: linear-gradient(135deg, var(--gold), var(--gold-dark));
  color: #000 !important;
  font-weight: 700;
  padding: 14px 16px;
  border-radius: 12px;
  text-align: center;
  text-decoration: none;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}"""
new_company = """.company-bill-btn {
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(20px) saturate(120%);
  -webkit-backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  border-left: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff !important;
  font-weight: 600;
  padding: 14px 20px;
  border-radius: 50px;
  text-align: center;
  text-decoration: none;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}"""
safe_replace(old_company, new_company)

old_company_hover = """.company-bill-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.5);
  color: #000 !important;
}"""
new_company_hover = """.company-bill-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3), inset 0 1px 2px rgba(255, 255, 255, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.45);
}"""
safe_replace(old_company_hover, new_company_hover)

old_tab = """.breakdown-tab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  background: var(--bg-card);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
}"""
new_tab = """.breakdown-tab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 50px;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.05);
}"""
safe_replace(old_tab, new_tab)

old_tab_hover = """.breakdown-tab:hover {
  border-color: var(--border-accent);
  color: var(--text-primary);
}"""
new_tab_hover = """.breakdown-tab:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
}"""
safe_replace(old_tab_hover, new_tab_hover)

old_tab_active = """.breakdown-tab.active {
  background: var(--gold-glow);
  border-color: var(--gold);
  color: var(--gold);
}"""
new_tab_active = """.breakdown-tab.active {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-top: 1px solid rgba(255, 255, 255, 0.4);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.3);
}"""
safe_replace(old_tab_active, new_tab_active)


with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated CSS company/tabs safely")
