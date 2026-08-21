import re

with open('dashboard.py', 'r') as f:
    content = f.read()

# 1. get_kpis
content = content.replace('''    prev_dates = [d for d in orders_by_date.keys() if d < now.date()]
    yesterday_orders = orders_by_date[max(prev_dates)] if prev_dates else 0''', '''    prev_dates = [d for d in orders_by_date.keys() if d < now.date()]
    yesterday_orders = orders_by_date[max(prev_dates)] if prev_dates else 0

    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        price = parse_price(row[18])
        total_revenue += price
        total_orders += 1
        dt = parse_date(row[8]) if len(row) > 8 else None
        if dt:
            d = dt.date()
            orders_by_date[d] = orders_by_date.get(d, 0) + 1
            if fy_start <= dt <= fy_end:
                this_year += 1
                this_year_rev += price
            if dt.year == current_year and dt.month == current_month:
                this_month += 1
                this_month_rev += price
            if dt.date() == now.date():
                today += 1
                today_rev += price''', 1)

# 2. companies_revenue
content = content.replace('''                    counts["today"][portal] = counts["today"].get(portal, 0) + 1''', '''                    counts["today"][portal] = counts["today"].get(portal, 0) + 1

    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        price = parse_price(row[18])
        if price > 0:
            portals["total"][portal] = portals["total"].get(portal, 0) + price
            if dt:
                if fy_start <= dt <= fy_end:
                    portals["year"][portal] = portals["year"].get(portal, 0) + price
                if dt.year == current_year and dt.month == current_month:
                    portals["month"][portal] = portals["month"].get(portal, 0) + price
                if dt.date() == today:
                    portals["today"][portal] = portals["today"].get(portal, 0) + price
                    counts["today"][portal] = counts["today"].get(portal, 0) + 1''', 1)

# 3. revenue_chart
content = content.replace('''            monthly_data[month_label]["order_count"] += 1''', '''            monthly_data[month_label]["order_count"] += 1
            
    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        price = parse_price(row[18])
        if dt and price > 0:
            month_label = dt.strftime("%b %Y")
            if month_label not in monthly_data:
                monthly_data[month_label] = {"month": month_label, "_dt": dt.replace(day=1), "order_count": 0}
            monthly_data[month_label][portal] = monthly_data[month_label].get(portal, 0) + price
            monthly_data[month_label]["order_count"] += 1''', 1)

# 4. recent_orders
content = content.replace('''        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)''', '''        })
        
    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        material = row[19].strip() if len(row) > 19 else ""
        size = row[10].strip() if len(row) > 10 else ""
        valid_orders.append({
            "id": f"c_{i}",
            "order_id": row[5].strip() if len(row) > 5 else f"C-ORD-{i}",
            "platform": (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": f"{material} {size}".strip(),
            "amount": parse_price(row[18]),
            "status": row[12].strip() if len(row) > 12 else "Unknown",
            "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt or datetime.min
        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)''', 1)

# 5. today_orders
content = content.replace('''        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)''', '''        })
        
    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        if not dt or dt.date() != today: continue
        material = row[19].strip() if len(row) > 19 else ""
        size = row[10].strip() if len(row) > 10 else ""
        valid_orders.append({
            "id": f"c_{i}",
            "order_id": row[5].strip() if len(row) > 5 else f"C-ORD-{i}",
            "platform": (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": f"{material} {size}".strip(),
            "amount": parse_price(row[18]),
            "status": row[12].strip() if len(row) > 12 else "Unknown",
            "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt
        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)''')

with open('dashboard.py', 'w') as f:
    f.write(content)
