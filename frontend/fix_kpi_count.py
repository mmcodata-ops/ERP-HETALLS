import sys
import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Comment out the 6th card (HETALLS Orders) to make it exactly 5 cards like the mockup
old_card = "<HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} />,"
new_card = "{/* <HetallsSpinningCard key=\"htl-ord\" companiesRev={companiesRev} isCurrency={false} style={{ viewTransitionName: 'kpi-htl-ord' }} /> */}"

code = code.replace(old_card, new_card)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Commented out HETALLS Orders card to force exactly 5 cards.")
