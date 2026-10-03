import sys
import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the invalid comment
old_comment = "{/* <HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} /> */},"
new_comment = "// <HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} />,"

if old_comment in code:
    code = code.replace(old_comment, new_comment)
else:
    print("Could not find the exact comment to fix. Trying regex.")
    code = code.replace("{/* <HetallsSpinningCard key=\"htl-ord\"", "// <HetallsSpinningCard key=\"htl-ord\"").replace("/> */},", "/>,")

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed JSX comment inside JS array.")
