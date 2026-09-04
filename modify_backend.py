import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Initialize order_count_hg and order_count_ho instead of order_count
content = re.sub(r'\"order_count\": 0', '"order_count_hg": 0, "order_count_ho": 0', content)

# Change order_count += 1 for HG companies
content = re.sub(r'monthly_data\[month_label\]\[\"order_count\"\] \+= 1', 'monthly_data[month_label]["order_count_hg"] += 1', content)

# Wait, the regex will replace all order_count += 1. But we want order_count_ho for Hetalls!
