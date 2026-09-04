import re

with open('dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

recent_logic = '''
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        dt = parse_date(row[8])
        if dt:
            valid_orders.append({
                "platform": normalize_portal(row[4]),
                "customer": row[6].strip() if len(row) > 6 else "",
                "amount": parse_price(row[26]),
                "order_date": row[8].strip() if len(row) > 8 else "",
                "_dt": dt
            })

'''

today_logic = '''
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        dt = parse_date(row[8])
        if dt and dt.date() == today:
            valid_orders.append({
                "platform": normalize_portal(row[4]),
                "customer": row[6].strip() if len(row) > 6 else "",
                "amount": parse_price(row[26]),
                "order_date": row[8].strip() if len(row) > 8 else "",
                "_dt": dt
            })

'''

# Inject recent_logic before the FIRST occurrence of valid_orders.sort
parts = content.split('    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)')
content = parts[0] + recent_logic + '    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)' + parts[1] + today_logic + '    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)' + parts[2]

with open('dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)

