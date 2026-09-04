import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix recent_orders
old_recent = '''def recent_orders(current_user=Depends(get_current_user)):
    orders_data = fetch_sheet_csv("ORDERS")
    valid_orders = []
    
    for i, row in enumerate(orders_data[1:]):
        if len(row) < 37: continue
        
        dt = parse_date(row[8])
        material = row[10].strip() if len(row) > 10 else ""
        size = row[11].strip() if len(row) > 11 else ""
        
        valid_orders.append({
            "id": i,
            "order_id": row[5].strip() if len(row) > 5 else f"ORD-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": f"{material} {size}".strip(),
            "amount": parse_price(row[36]),
            "status": row[14].strip() if len(row) > 14 else "Unknown",
            "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt or datetime.min
        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)
    
    for o in valid_orders:
        del o["_dt"]
        
    return valid_orders[:10]'''

new_recent = '''def recent_orders(current_user=Depends(get_current_user)):
    orders_data = fetch_sheet_csv("ORDERS")
    valid_orders = []
    
    for i, row in enumerate(orders_data[1:]):
        if len(row) < 37: continue
        dt = parse_date(row[8])
        material = row[10].strip() if len(row) > 10 else ""
        size = row[11].strip() if len(row) > 11 else ""
        valid_orders.append({
            "id": f"ord-{i}", "order_id": row[5].strip() if len(row) > 5 else f"ORD-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": f"{material} {size}".strip(), "amount": parse_price(row[36]),
            "status": row[14].strip() if len(row) > 14 else "Unknown", "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt or datetime.min
        })

    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for i, row in enumerate(mkm_orders_data[1:]):
        if len(row) < 27: continue
        dt = parse_date(row[8])
        valid_orders.append({
            "id": f"mkm-{i}", "order_id": row[1].strip() if len(row) > 1 else f"MKM-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "ETSY-MKM",
            "customer_name": row[7].strip() if len(row) > 7 else "Unknown",
            "product_name": row[12].strip() if len(row) > 12 else "Unknown", "amount": parse_price(row[26]),
            "status": row[14].strip() if len(row) > 14 else "Unknown", "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt or datetime.min
        })
        
    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8])
        valid_orders.append({
            "id": f"cpt-{i}", "order_id": row[5].strip() if len(row) > 5 else f"CPT-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "EBAY-CASAVANI (CARPET)",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": row[10].strip() if len(row) > 10 else "Unknown", "amount": parse_price(row[18]),
            "status": row[12].strip() if len(row) > 12 else "Unknown", "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt or datetime.min
        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)
    for o in valid_orders: del o["_dt"]
    return valid_orders[:10]'''

if old_recent in content:
    content = content.replace(old_recent, new_recent)
    print("Fixed recent_orders!")
else:
    print("recent_orders not found!")

# Fix today_orders
old_today = '''def today_orders(current_user=Depends(get_current_user)):
    orders_data = fetch_sheet_csv("ORDERS")
    valid_orders = []
    
    today = datetime.now().date()
    
    for i, row in enumerate(orders_data[1:]):
        if len(row) < 37: continue
        
        dt = parse_date(row[8])
        if not dt or dt.date() != today: continue
        
        material = row[10].strip() if len(row) > 10 else ""
        size = row[11].strip() if len(row) > 11 else ""
        
        valid_orders.append({
            "id": i,
            "order_id": row[5].strip() if len(row) > 5 else f"ORD-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": f"{material} {size}".strip(),
            "amount": parse_price(row[36]),
            "status": row[14].strip() if len(row) > 14 else "Unknown",
            "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt
        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)
    
    for o in valid_orders:
        del o["_dt"]
        
    return valid_orders'''

new_today = '''def today_orders(current_user=Depends(get_current_user)):
    orders_data = fetch_sheet_csv("ORDERS")
    valid_orders = []
    today = datetime.utcnow().date()
    
    for i, row in enumerate(orders_data[1:]):
        if len(row) < 37: continue
        dt = parse_date(row[8])
        if not dt or dt.date() != today: continue
        material = row[10].strip() if len(row) > 10 else ""
        size = row[11].strip() if len(row) > 11 else ""
        valid_orders.append({
            "id": f"ord-{i}", "order_id": row[5].strip() if len(row) > 5 else f"ORD-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": f"{material} {size}".strip(), "amount": parse_price(row[36]),
            "status": row[14].strip() if len(row) > 14 else "Unknown", "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt
        })

    mkm_orders_data = fetch_mkm_orders_sheet_csv()
    for i, row in enumerate(mkm_orders_data[1:]):
        if len(row) < 27: continue
        dt = parse_date(row[8])
        if not dt or dt.date() != today: continue
        valid_orders.append({
            "id": f"mkm-{i}", "order_id": row[1].strip() if len(row) > 1 else f"MKM-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "ETSY-MKM",
            "customer_name": row[7].strip() if len(row) > 7 else "Unknown",
            "product_name": row[12].strip() if len(row) > 12 else "Unknown", "amount": parse_price(row[26]),
            "status": row[14].strip() if len(row) > 14 else "Unknown", "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt
        })

    carpet_data = fetch_carpet_sheet_csv()
    for i, row in enumerate(carpet_data[1:]):
        if len(row) < 19: continue
        dt = parse_date(row[8])
        if not dt or dt.date() != today: continue
        valid_orders.append({
            "id": f"cpt-{i}", "order_id": row[5].strip() if len(row) > 5 else f"CPT-{i}",
            "platform": normalize_portal(row[4]) if len(row) > 4 else "EBAY-CASAVANI (CARPET)",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",
            "product_name": row[10].strip() if len(row) > 10 else "Unknown", "amount": parse_price(row[18]),
            "status": row[12].strip() if len(row) > 12 else "Unknown", "order_date": row[8].strip() if len(row) > 8 else "",
            "_dt": dt
        })
        
    valid_orders.sort(key=lambda x: x["_dt"], reverse=True)
    for o in valid_orders: del o["_dt"]
    return valid_orders'''

if old_today in content:
    content = content.replace(old_today, new_today)
    print("Fixed today_orders!")
else:
    print("today_orders not found!")

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
