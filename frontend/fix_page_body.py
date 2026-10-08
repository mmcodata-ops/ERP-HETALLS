import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The user explicitly asked to fix the issue where:
# @media (width <= 900px) {
#   .page-body {
#       padding: 16px 20px !important;
#   }
# }
# causes layout disturbances.

# Let's remove any .page-body overrides inside media queries that set padding: 16px 20px !important;
css = re.sub(r'\.page-body\s*\{\s*padding:\s*16px\s*20px\s*!important;\s*\}', '', css)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed the problematic .page-body padding override.")
