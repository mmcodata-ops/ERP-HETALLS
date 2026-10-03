import sys
import re

# 1. Restore the 6th tab in Dashboard.jsx
with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_comment = "// <HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} />,"
new_element = "<HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} />,"

if old_comment in code:
    code = code.replace(old_comment, new_element)
else:
    print("Warning: Could not find the commented out HETALLS Orders card.")

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)


# 2. Update the grid to 6 columns but keep the aesthetic in index.css
with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change repeat(5, 1fr) to repeat(6, 1fr)
css = re.sub(r"grid-template-columns:\s*repeat\(5,\s*1fr\);", "grid-template-columns: repeat(6, 1fr);", css)

# Reduce the inner padding slightly so the 6 cards don't cramp the text
css = re.sub(r"padding:\s*20px\s*24px\s*!important;", "padding: 16px 16px !important;", css)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored 6th tab and updated CSS grid to 6 columns while keeping exact mockup aesthetics.")
