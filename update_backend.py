import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace initialization inside revenue_chart
content = content.replace('"_dt": dt.replace(day=1), "order_count": 0}',
                          '"_dt": dt.replace(day=1), "order_count_hg": 0, "order_count_ho": 0}')

# Now replace the specific increments.
# We know lines 575, 591, 611 are HG orders. Line 628 is Hetalls.
# It's safer to just replace all monthly_data[month_label]["order_count"] += 1 with monthly_data[month_label]["order_count_hg"] += 1 first.
content = content.replace('monthly_data[month_label]["order_count"] += 1', 'monthly_data[month_label]["order_count_hg"] += 1')

# Then for the Hetalls block, find it and change it to order_count_ho.
# The Hetalls block starts with "# Add Hetalls orders"
hetalls_split = content.split('# Add Hetalls orders')
if len(hetalls_split) > 1:
    hetalls_block = hetalls_split[1]
    hetalls_block = hetalls_block.replace('monthly_data[month_label]["order_count_hg"] += 1', 'monthly_data[month_label]["order_count_ho"] += 1')
    content = hetalls_split[0] + '# Add Hetalls orders' + hetalls_block

# Update the rounding skip logic
content = content.replace('if k != "month" and k != "order_count":', 'if k != "month" and k != "order_count_hg" and k != "order_count_ho":')

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated backend for separated order_count_hg and order_count_ho")
