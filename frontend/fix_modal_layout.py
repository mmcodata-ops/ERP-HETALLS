import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the breakdown-tab-custom CSS
old_css = """.breakdown-tab-custom {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: auto;
  }"""

new_css = """.breakdown-tab-custom {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: 8px;
    padding-left: 16px;
    border-left: 1px solid rgba(255, 255, 255, 0.1);
  }"""

if old_css in css:
    css = css.replace(old_css, new_css)
else:
    # Fallback regex
    css = re.sub(
        r'\.breakdown-tab-custom\s*\{[^}]*margin-left:\s*auto;[^}]*\}',
        new_css,
        css
    )

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated breakdown-tab-custom CSS")
