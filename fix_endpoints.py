with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix get_kpis
kpis_bad = '''                if dt.year == current_year and dt.month == current_month:
                    this_month_revenue += price
                if dt.year == current_year:
                    this_year_revenue += price
                if dt.date() == today:
                    today_revenue += price'''
kpis_good = '''                if dt.year == current_year and dt.month == current_month:
                    this_month_rev += price
                if dt.year == current_year:
                    this_year_rev += price
                if dt.date() == today:
                    today_rev += price'''
content = content.replace(kpis_bad, kpis_good)

# Fix companies_revenue
comp_bad = '''            if dt:
                if dt.year == current_year and dt.month == current_month:
                    portals["thisMonth"][portal] = portals["thisMonth"].get(portal, 0) + price
                    counts["thisMonth"][portal] = counts["thisMonth"].get(portal, 0) + 1
                if dt.year == current_year:
                    portals["thisYear"][portal] = portals["thisYear"].get(portal, 0) + price
                    counts["thisYear"][portal] = counts["thisYear"].get(portal, 0) + 1
                if dt.date() == today:
                    portals["today"][portal] = portals["today"].get(portal, 0) + price
                    counts["today"][portal] = counts["today"].get(portal, 0) + 1'''
                    
comp_good = '''            if dt:
                if fy_start <= dt <= fy_end:
                    portals["year"][portal] = portals["year"].get(portal, 0) + price
                if dt.year == current_year and dt.month == current_month:
                    portals["month"][portal] = portals["month"].get(portal, 0) + price
                if dt.date() == today:
                    portals["today"][portal] = portals["today"].get(portal, 0) + price
                    counts["today"][portal] = counts["today"].get(portal, 0) + 1'''
content = content.replace(comp_bad, comp_good)

# Fix recent/today orders
orders_bad = '''            valid_orders.append({
                "platform": normalize_portal(row[4]),
                "customer": row[6].strip() if len(row) > 6 else "",
                "amount": parse_price(row[26]),
                "order_date": row[8].strip() if len(row) > 8 else "",
                "_dt": dt
            })'''

def generate_orders_good(prefix):
    return f'''            material = row[10].strip() if len(row) > 10 else ""
            size = row[11].strip() if len(row) > 11 else ""
            valid_orders.append({{
                "id": f"{prefix}_" + (row[5].strip() if len(row) > 5 else "unknown"),
                "order_id": row[5].strip() if len(row) > 5 else "Unknown",
                "platform": normalize_portal(row[4]),
                "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
                "product_name": f"{{material}} {{size}}".strip(),
                "amount": parse_price(row[26]),
                "status": row[14].strip() if len(row) > 14 else "Unknown",
                "order_date": row[8].strip() if len(row) > 8 else "",
                "_dt": dt
            }})'''

# It appears twice, so we replace them one by one
parts = content.split(orders_bad)
if len(parts) == 3:
    content = parts[0] + generate_orders_good('mkm_recent') + parts[1] + generate_orders_good('mkm_today') + parts[2]
else:
    print(f"Expected 2 occurrences of orders_bad, found {len(parts)-1}")

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
