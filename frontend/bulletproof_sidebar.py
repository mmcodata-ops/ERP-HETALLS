import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the hiding logic bulletproof
css = css.replace(
    "transform: translateX(-110%);",
    "transform: translateX(-110%) !important;"
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added !important to sidebar hide transform.")
