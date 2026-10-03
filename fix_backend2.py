import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace initialization inside revenue_chart
content = content.replace('"_dt": dt.replace(day=1), "order_count": 0}',
                          '"_dt": dt.replace(day=1), "order_count_hg": 0, "order_count_ho": 0}')

# Now replace the specific increments carefully.
# In revenue_chart, there are four blocks adding to monthly_data:
# 1. Main ORDERS
# 2. CARPET
# 3. MKM
# 4. HETALLS

# We can safely use regex to replace it line by line based on context.
lines = content.split('\n')
in_hetalls_block = False
new_lines = []

for line in lines:
    if 'Add Hetalls orders' in line:
        in_hetalls_block = True
    elif 'Sort by date' in line:
        in_hetalls_block = False
        
    if 'monthly_data[month_label]["order_count"] += 1' in line:
        if in_hetalls_block:
            line = line.replace('"order_count"', '"order_count_ho"')
        else:
            line = line.replace('"order_count"', '"order_count_hg"')
            
    if 'if k != "month" and k != "order_count":' in line:
        line = line.replace('if k != "month" and k != "order_count":', 'if k != "month" and k != "order_count_hg" and k != "order_count_ho":')
        
    new_lines.append(line)

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Fixed backend")
