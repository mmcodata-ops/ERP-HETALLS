import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the mkm loop in get_kpis
old_mkm = '''    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        status = row[14].strip().lower() if len(row) > 14 else ""
        if status == "returned": continue
        
        dt = parse_date(row[8])
        portal = normalize_portal(row[4])
        price = parse_price(row[26])
        
        if price > 0:
            total_revenue += price
            if dt:
                if dt.year == current_year and dt.month == current_month:
                    this_month_rev += price
                if dt.year == current_year:
                    this_year_rev += price
                if dt.date() == today:
                    today_rev += price'''

new_mkm = '''    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        status = row[14].strip().lower() if len(row) > 14 else ""
        if status == "returned": continue
        
        dt = parse_date(row[8])
        portal = normalize_portal(row[4])
        price = parse_price(row[26])
        
        if price > 0:
            total_revenue += price
            total_orders += 1
            if dt:
                if fy_start <= dt <= fy_end:
                    this_year += 1
                    this_year_rev += price
                if dt.year == current_year and dt.month == current_month:
                    this_month += 1
                    this_month_rev += price
                if dt.date() == now.date():
                    today += 1
                    today_rev += price'''

if old_mkm in content:
    content = content.replace(old_mkm, new_mkm)
    with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found! Here is what it looks like:")
    print(content[content.find('mkm_orders_data = fetch_mkm_orders_sheet_csv()'):content.find('return', content.find('mkm_orders_data = fetch_mkm_orders_sheet_csv()'))])
