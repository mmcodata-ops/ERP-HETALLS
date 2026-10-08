import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the vision-bg variable and the body override that was injected
# Replace --vision-bg: #000000 with the original bg-base
css = css.replace("--vision-bg: #000000;", "--vision-bg: #050811;")

# Also make sure login-page has a proper visible background
css = css.replace(
    "background: var(--bg-base);",
    "background: #050811;"
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed vision-bg variable.")
