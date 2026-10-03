import re

with open('backend/routers/breakdown.py', 'r', encoding='utf-8') as f:
    code = f.read()

new_func = """
def process_items_for_breakdown(row, sheet_type, target_date, image_map, items):
    if sheet_type == 'ORDERS':
        if len(row) < 37: return
        status = row[14].strip().lower() if len(row) > 14 else ""
        date_col, portal_col, order_col, buyer_col, mat_col, size_col, qty_col, price_col, pic_col1, pic_col2 = 8, 4, 5, 6, 10, 11, 9, 36, 18, 7
    elif sheet_type == 'CARPET':
        if len(row) < 19: return
        status = row[12].strip().lower() if len(row) > 12 else ""
        date_col, portal_col, order_col, buyer_col, mat_col, size_col, qty_col, price_col, pic_col1, pic_col2 = 8, 4, 5, 6, 10, 11, 9, 18, 17, 7 # Approximated columns for carpet pic
    elif sheet_type == 'MKM':
        if len(row) < 27: return
        status = row[14].strip().lower() if len(row) > 14 else ""
        date_col, portal_col, order_col, buyer_col, mat_col, size_col, qty_col, price_col, pic_col1, pic_col2 = 8, 4, 1, 7, 12, 13, 9, 26, 17, 7
    
    if status == "returned": return
    
    row_dt = parse_date(row[date_col] if len(row) > date_col else "")
    if not row_dt or row_dt.date() != target_date: return
    
    price = parse_price(row[price_col] if len(row) > price_col else 0)
    if price <= 0: return
    
    order_no = row[order_col].strip() if len(row) > order_col else ""
    pic = image_map.get(order_no, "")
    if not pic:
        pic = (row[pic_col1].strip() if len(row) > pic_col1 and row[pic_col1].strip() else (row[pic_col2].strip() if len(row) > pic_col2 else ""))
    
    portal = normalize_portal(row[portal_col] if len(row) > portal_col else "")
    if sheet_type == 'CARPET':
        portal = f"{portal} (CARPET)"
        
    items.append({
        "portal": portal,
        "order_no": order_no,
        "buyer_name": row[buyer_col].strip() if len(row) > buyer_col else "",
        "picture": pic,
        "material": row[mat_col].strip() if len(row) > mat_col else "",
        "size": row[size_col].strip() if len(row) > size_col else "",
        "quantity": row[qty_col].strip() if len(row) > qty_col else "",
        "price": price
    })

@router.get("/daily-sales-items")
def daily_sales_items(date: str = Query(...), current_user=Depends(get_current_user)):
    target_dt = parse_date(date)
    if not target_dt:
        return []
        
    target_date = target_dt.date()
    image_map = _fetch_image_urls()
    items = []
    
    data = fetch_sheet_csv("ORDERS")
    if data and len(data) > 1:
        for row in data[1:]: process_items_for_breakdown(row, 'ORDERS', target_date, image_map, items)
        
    carpet_data = fetch_carpet_sheet_csv()
    if carpet_data and len(carpet_data) > 1:
        for row in carpet_data[1:]: process_items_for_breakdown(row, 'CARPET', target_date, image_map, items)
        
    mkm_data = fetch_mkm_orders_sheet_csv()
    if mkm_data and len(mkm_data) > 1:
        for row in mkm_data[1:]: process_items_for_breakdown(row, 'MKM', target_date, image_map, items)
        
    return items
"""

# Regex to find everything from @router.get("/daily-sales-items") to the end of the file
pattern = re.compile(r'@router\.get\("/daily-sales-items"\).*', re.DOTALL)

if pattern.search(code):
    new_code = pattern.sub(new_func + '\n', code)
    with open('backend/routers/breakdown.py', 'w', encoding='utf-8') as f:
        f.write(new_code)
    print("Successfully replaced daily_sales_items logic!")
else:
    print("Could not find daily_sales_items function to replace.")
