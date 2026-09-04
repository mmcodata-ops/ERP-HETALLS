import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove mkm_data from get_kpis
pattern1 = r'    mkm_data = fetch_mkm_sheet_csv\(\).*?today_rev \+= daily_mkm_rev\n'
content = re.sub(pattern1, '', content, flags=re.DOTALL)

# Remove mkm_data from companies_revenue
pattern2 = r'    mkm_data = fetch_mkm_sheet_csv\(\).*?portals\["today"\]\[portal\] = portals\["today"\].get\(portal, 0\) \+ price\n'
content = re.sub(pattern2, '', content, flags=re.DOTALL)

# Remove mkm_data from revenue_chart
pattern3 = r'    mkm_data = fetch_mkm_sheet_csv\(\).*?monthly_data\[month_label\]\[portal\] = monthly_data\[month_label\].get\(portal, 0\) \+ price\n'
content = re.sub(pattern3, '', content, flags=re.DOTALL)

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
