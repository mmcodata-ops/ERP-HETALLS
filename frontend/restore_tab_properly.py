import sys
import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the messy comment to restore the element
code = re.sub(
    r"//\s*<HetallsSpinningCard key=\"htl-ord\".*?/> \*/\}",
    "<HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} />,",
    code
)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Properly restored HETALLS Orders card.")
