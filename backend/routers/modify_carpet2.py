import re

with open('dashboard.py', 'r') as f:
    content = f.read()

content = content.replace('''    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        price = parse_price(row[18])
        if price > 0:
            portals["total"][portal] = portals["total"].get(portal, 0) + price''', '''    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        portal = f"{portal} (CARPET)"
        price = parse_price(row[18])
        if price > 0:
            portals["total"][portal] = portals["total"].get(portal, 0) + price''')

content = content.replace('''    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        price = parse_price(row[18])
        if dt and price > 0:
            month_label = dt.strftime("%b %Y")''', '''    carpet_data = fetch_carpet_sheet_csv()
    for row in carpet_data[1:]:
        if len(row) < 19: continue
        status = row[12].strip().lower() if len(row) > 12 else ""
        if status == "returned": continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        portal = f"{portal} (CARPET)"
        price = parse_price(row[18])
        if dt and price > 0:
            month_label = dt.strftime("%b %Y")''')

content = content.replace('''    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        material = row[19].strip() if len(row) > 19 else ""
        size = row[10].strip() if len(row) > 10 else ""
        valid_orders.append({
            "id": f"c_{i}",
            "order_id": row[5].strip() if len(row) > 5 else f"C-ORD-{i}",
            "platform": (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN",''', '''    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        material = row[19].strip() if len(row) > 19 else ""
        size = row[10].strip() if len(row) > 10 else ""
        valid_orders.append({
            "id": f"c_{i}",
            "order_id": row[5].strip() if len(row) > 5 else f"C-ORD-{i}",
            "platform": ((row[4].strip() or "UNKNOWN").upper() + " (CARPET)") if len(row) > 4 else "UNKNOWN (CARPET)",''')

content = content.replace('''    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        if not dt or dt.date() != today: continue
        material = row[19].strip() if len(row) > 19 else ""
        size = row[10].strip() if len(row) > 10 else ""
        valid_orders.append({
            "id": f"c_{i}",
            "order_id": row[5].strip() if len(row) > 5 else f"C-ORD-{i}",
            "platform": (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN",''', '''    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8]) if len(row) > 8 else None
        if not dt or dt.date() != today: continue
        material = row[19].strip() if len(row) > 19 else ""
        size = row[10].strip() if len(row) > 10 else ""
        valid_orders.append({
            "id": f"c_{i}",
            "order_id": row[5].strip() if len(row) > 5 else f"C-ORD-{i}",
            "platform": ((row[4].strip() or "UNKNOWN").upper() + " (CARPET)") if len(row) > 4 else "UNKNOWN (CARPET)",''')

with open('dashboard.py', 'w') as f:
    f.write(content)
