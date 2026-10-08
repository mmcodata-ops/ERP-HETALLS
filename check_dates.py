import sys
sys.path.insert(0, './backend')
from routers.dashboard import fetch_sheet_csv, parse_date, parse_price
from datetime import datetime

orders = fetch_sheet_csv('ORDERS')
now = datetime.now()
print('Now day:', now.day)

sep_total = 0
sep_filtered = 0

for row in orders[1:]:
    dt = parse_date(row[8]) if len(row) > 8 else None
    if not dt or dt.month != 9: continue
    
    price = parse_price(row[36]) if len(row) > 36 else 0
    sep_total += price
    
    if dt.day <= now.day:
        sep_filtered += price

print(f"Sep total: {sep_total}")
print(f"Sep filtered (<= {now.day}): {sep_filtered}")
