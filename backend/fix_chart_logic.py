import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace `if dt and price > 0:` with `if dt:` in the revenue_chart function
# We should probably be careful to only replace it in revenue_chart, but it looks like 
# all 4 occurrences are in revenue_chart since get_kpis doesn't have it.

new_content = content.replace("if dt and price > 0:", "if dt:")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated backend to include all orders in revenue chart regardless of price.")
