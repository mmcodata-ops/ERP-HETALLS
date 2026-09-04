import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Filter PieChart data
content = content.replace('data={companiesRev.today}', 'data={companiesRev.today.filter(c => !c.name?.toUpperCase().includes(\\\'HETALLS\\\'))}')

# Let's also filter the RevenueSpinningCard which takes companiesRev
content = content.replace('companiesRev={companiesRev}', 'companiesRev={companiesRev ? { today: companiesRev.today?.filter(c => !c.name?.toUpperCase().includes(\\\'HETALLS\\\')), month: companiesRev.month?.filter(c => !c.name?.toUpperCase().includes(\\\'HETALLS\\\')), year: companiesRev.year?.filter(c => !c.name?.toUpperCase().includes(\\\'HETALLS\\\')), total: companiesRev.total?.filter(c => !c.name?.toUpperCase().includes(\\\'HETALLS\\\')) } : null}')

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Dashboard.jsx")
