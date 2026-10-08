import sys

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the sidebar mobile slide transition with the same water curve
css = css.replace(
    "transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1) !important;",
    "transition: transform 0.5s cubic-bezier(0.4, 0, 0, 1) !important;"
)

# Also update the vision-spring variable
css = css.replace(
    "--vision-spring: cubic-bezier(0.22, 1, 0.36, 1);",
    "--vision-spring: cubic-bezier(0.4, 0, 0, 1);"
)

# Update nav-item active styling — remove the old hard background swap, let the pill handle it
css = css.replace(
    "transition: all 0.4s var(--vision-spring);",
    "transition: all 0.5s cubic-bezier(0.4, 0, 0, 1);"
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied water-smooth curves to CSS globally.")
