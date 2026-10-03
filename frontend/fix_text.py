import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

def safe_replace(old, new, count=1):
    global css
    if old not in css:
        print(f"Warning: could not find {old[:40]}")
    css = css.replace(old, new, count)

old_text = """  --text-primary:  #f8fafc;
  --text-secondary:#cbd5e1;
  --text-muted:    #64748b;"""

new_text = """  --text-primary:  #ffffff;
  --text-secondary:#e2e8f0;
  --text-muted:    #94a3b8;"""

safe_replace(old_text, new_text)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Text colors brightened")
