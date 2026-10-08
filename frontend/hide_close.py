import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
@media (min-width: 901px) {
  .tooltip-close-btn { display: none !important; }
}
"""

if '.tooltip-close-btn' not in css:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css + new_css)
    print("Added tooltip-close-btn hide rule")
