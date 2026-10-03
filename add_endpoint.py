import re

with open('backend/routers/breakdown.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_endpoint = '''
@router.get("/daily-sales-items")
def daily_sales_items(date: str = Query(...), current_user=Depends(get_current_user)):
    data = fetch_sheet_csv("ORDERS")
    if not data or len(data) < 2:
        return []
        
    target_dt = parse_date(date)
    if not target_dt:
        return []
        
    target_date = target_dt.date()
    items = []
    
    for row in data[1:]:
        if len(row) < 37: continue
        status = row[14].strip().lower() if len(row) > 14 else ""
        if status == "returned": continue
        
        row_dt = parse_date(row[8])
        if not row_dt or row_dt.date() != target_date: continue
        
        price = parse_price(row[36])
        if price <= 0: continue
        
        items.append({
            "portal": row[4].strip(),
            "order_no": row[5].strip(),
            "buyer_name": row[6].strip(),
            "picture": row[7].strip(),
            "material": row[10].strip(),
            "size": row[11].strip(),
            "quantity": row[9].strip(),
            "price": price
        })
        
    return items
'''

content += '\\n' + new_endpoint

with open('backend/routers/breakdown.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Endpoint added")
