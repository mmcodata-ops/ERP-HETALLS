with open('dashboard.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# recent orders
recent = []
in_recent = False
for line in lines:
    if 'def recent_orders(' in line:
        in_recent = True
    if in_recent:
        recent.append(line)
        if 'return orders' in line:
            break
print('RECENT ORDERS:')
print(''.join(recent[-10:]))

# today orders
today = []
in_today = False
for line in lines:
    if 'def today_orders(' in line:
        in_today = True
    if in_today:
        today.append(line)
        if 'return orders' in line:
            break
print('TODAY ORDERS:')
print(''.join(today[-10:]))
