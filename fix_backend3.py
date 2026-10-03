import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure they are all correctly set
# First, change all order_count_ho back to order_count to normalize
content = content.replace('monthly_data[month_label]["order_count_ho"] += 1', 'monthly_data[month_label]["order_count"] += 1')
content = content.replace('monthly_data[month_label]["order_count_hg"] += 1', 'monthly_data[month_label]["order_count"] += 1')

lines = content.split('\n')
new_lines = []

in_revenue_chart = False
in_hetalls = False

for line in lines:
    if 'def revenue_chart' in line:
        in_revenue_chart = True
        
    if in_revenue_chart and 'Add Hetalls orders' in line:
        in_hetalls = True
        
    if in_revenue_chart and 'Sort by date' in line:
        in_hetalls = False
        in_revenue_chart = False

    if 'monthly_data[month_label]["order_count"] += 1' in line:
        if in_hetalls:
            line = line.replace('"order_count"', '"order_count_ho"')
        else:
            line = line.replace('"order_count"', '"order_count_hg"')
            
    new_lines.append(line)

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Fixed backend carefully")
