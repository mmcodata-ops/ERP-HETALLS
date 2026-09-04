import re

with open('dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

mkm_func = '''
def fetch_mkm_orders_sheet_csv():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
    try:
        response = urllib.request.urlopen(url)
        csv_data = response.read().decode('utf-8')
        reader = csv.reader(csv_data.splitlines())
        return list(reader)
    except Exception as e:
        print(f"Error fetching MKM orders sheet: {e}")
        return []

'''
content = content.replace('def fetch_mkm_sheet_csv():', mkm_func + 'def fetch_mkm_sheet_csv():')

def inject_code(target_str, insert_str, text, count=1):
    return text.replace(target_str, insert_str + target_str, count)

kpi_logic = '''
    # Add MKM detailed orders
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
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
                    this_month_revenue += price
                if dt.year == current_year:
                    this_year_revenue += price
                if dt.date() == today:
                    today_revenue += price

'''
content = inject_code('    mkm_data = fetch_mkm_sheet_csv()', kpi_logic, content, 1)

comp_logic = '''
    # Add MKM detailed orders
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        status = row[14].strip().lower() if len(row) > 14 else ""
        if status == "returned": continue
        
        dt = parse_date(row[8])
        portal = normalize_portal(row[4])
        price = parse_price(row[26])
        
        if price > 0:
            portals["total"][portal] = portals["total"].get(portal, 0) + price
            counts["total"][portal] = counts["total"].get(portal, 0) + 1
            if dt:
                if dt.year == current_year and dt.month == current_month:
                    portals["thisMonth"][portal] = portals["thisMonth"].get(portal, 0) + price
                    counts["thisMonth"][portal] = counts["thisMonth"].get(portal, 0) + 1
                if dt.year == current_year:
                    portals["thisYear"][portal] = portals["thisYear"].get(portal, 0) + price
                    counts["thisYear"][portal] = counts["thisYear"].get(portal, 0) + 1
                if dt.date() == today:
                    portals["today"][portal] = portals["today"].get(portal, 0) + price
                    counts["today"][portal] = counts["today"].get(portal, 0) + 1

'''
# Replace the SECOND occurrence of mkm_data = fetch_mkm_sheet_csv()
parts = content.split('    mkm_data = fetch_mkm_sheet_csv()')
content = parts[0] + '    mkm_data = fetch_mkm_sheet_csv()' + parts[1] + comp_logic + '    mkm_data = fetch_mkm_sheet_csv()' + parts[2] + '    mkm_data = fetch_mkm_sheet_csv()' + parts[3]

chart_logic = '''
    # Add MKM detailed orders
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        status = row[14].strip().lower() if len(row) > 14 else ""
        if status == "returned": continue
        
        dt = parse_date(row[8])
        portal = normalize_portal(row[4])
        price = parse_price(row[26])
        
        if dt and price > 0:
            month_label = dt.strftime("%b %Y")
            if month_label not in monthly_data:
                monthly_data[month_label] = {"month": month_label, "_dt": dt.replace(day=1), "order_count": 0}
            monthly_data[month_label][portal] = monthly_data[month_label].get(portal, 0) + price
            monthly_data[month_label]["order_count"] += 1

'''
# Replace the THIRD occurrence
parts = content.split('    mkm_data = fetch_mkm_sheet_csv()')
content = parts[0] + '    mkm_data = fetch_mkm_sheet_csv()' + parts[1] + '    mkm_data = fetch_mkm_sheet_csv()' + parts[2] + chart_logic + '    mkm_data = fetch_mkm_sheet_csv()' + parts[3]

recent_logic = '''
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        dt = parse_date(row[8])
        if dt:
            orders.append({
                "date": dt,
                "order_no": row[5].strip() if len(row) > 5 else "",
                "customer": row[6].strip() if len(row) > 6 else "",
                "platform": normalize_portal(row[4]),
                "status": row[14].strip().upper() if len(row) > 14 else "",
                "amount": parse_price(row[26])
            })

'''
content = inject_code('    orders.sort(key=lambda x: x["date"], reverse=True)', recent_logic, content, 1)

today_logic = '''
    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for row in mkm_orders_data[1:]:
        if len(row) < 27: continue
        dt = parse_date(row[8])
        if dt and dt.date() == today:
            orders.append({
                "order_no": row[5].strip() if len(row) > 5 else "",
                "customer": row[6].strip() if len(row) > 6 else "",
                "platform": normalize_portal(row[4]),
                "status": row[14].strip().upper() if len(row) > 14 else "",
                "amount": parse_price(row[26])
            })

'''
content = content.replace('    return orders', today_logic + '    return orders')

with open('dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)

