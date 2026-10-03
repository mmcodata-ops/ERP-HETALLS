import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new):
    global css
    if old not in css:
        print(f"Warning: could not find exact match for \n{old[:80]}...\n")
    css = css.replace(old, new, 1)

# .btn-primary
old_btn = """.btn-primary {
  width: 100%; padding: 13px;
  background: linear-gradient(135deg, var(--gold), var(--gold-dark));
  color: #000; font-size: 15px; font-weight: 700;
  border-radius: var(--radius-sm);
  transition: all var(--transition);
  box-shadow: 0 4px 16px rgba(245,158,11,0.3);
}"""
new_btn = """.btn-primary {
  width: 100%; padding: 14px 20px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px) saturate(120%);
  -webkit-backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-top: 1px solid rgba(255, 255, 255, 0.35);
  border-left: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff; font-size: 15px; font-weight: 600;
  border-radius: 50px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 1px 2px rgba(255, 255, 255, 0.2);
  display: flex; align-items: center; justify-content: center; gap: 8px;
}"""
safe_replace(old_btn, new_btn)

old_btn_hover = """.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(245,158,11,0.4); }"""
new_btn_hover = """.btn-primary:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3), inset 0 1px 2px rgba(255, 255, 255, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.45);
}"""
safe_replace(old_btn_hover, new_btn_hover)

# .form-input
old_input = """.form-input {
  width: 100%; padding: 12px 14px;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  color: var(--text-primary); font-size: 14px;
  transition: border-color var(--transition);
}"""
new_input = """.form-input {
  width: 100%; padding: 14px 20px;
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  border-left: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 50px;
  color: #ffffff; font-size: 14px;
  transition: all 0.3s ease;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}"""
safe_replace(old_input, new_input)

old_input_focus = """.form-input:focus { border-color: var(--gold); box-shadow: 0 0 0 3px var(--gold-glow); }"""
new_input_focus = """.form-input:focus {
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.05);
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.1), inset 0 2px 4px rgba(0, 0, 0, 0.2);
}"""
safe_replace(old_input_focus, new_input_focus)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated CSS buttons safely")
