import re

with open('backend/routers/breakdown.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Make sure we have the imports
if "fetch_carpet_sheet_csv" not in code:
    code = code.replace(
        "from .dashboard import fetch_sheet_csv, parse_date, parse_price",
        "from .dashboard import fetch_sheet_csv, parse_date, parse_price, fetch_carpet_sheet_csv, fetch_mkm_orders_sheet_csv, normalize_portal"
    )

new_func = """
def process_row_for_breakdown(row, sheet_type, aggregated, unique_combinations, date, now):
    if sheet_type == 'ORDERS':
        if len(row) < 37: return
        status = row[14].strip().lower() if len(row) > 14 else ""
        date_col, portal_col, mat_col, price_col = 8, 4, 10, 36
    elif sheet_type == 'CARPET':
        if len(row) < 19: return
        status = row[12].strip().lower() if len(row) > 12 else ""
        date_col, portal_col, mat_col, price_col = 8, 4, 10, 18
    elif sheet_type == 'MKM':
        if len(row) < 27: return
        status = row[14].strip().lower() if len(row) > 14 else ""
        date_col, portal_col, mat_col, price_col = 8, 4, 12, 26
    
    if status == "returned": return
    
    row_dt = parse_date(row[date_col])
    if not row_dt: return
    
    row_date_obj = row_dt.date()
    if date == "today":
        if row_date_obj != now.date(): return
    elif date == "all":
        pass
    elif date.startswith("month|"):
        parts = date.split("|")[1].split("-")
        if row_date_obj.year != int(parts[0]) or row_date_obj.month != int(parts[1]): return
    else:
        try:
            parts = date.split("|")
            start_dt = datetime.strptime(parts[0], "%Y-%m-%d").date()
            end_dt = datetime.strptime(parts[1], "%Y-%m-%d").date() if len(parts) > 1 else start_dt
            if row_date_obj < start_dt or row_date_obj > end_dt: return
        except ValueError:
            return
            
    portal = normalize_portal(row[portal_col] if len(row) > portal_col else "").upper()
    if sheet_type == 'CARPET':
        portal = f"{portal} (CARPET)"
        
    material = (row[mat_col].strip() if len(row) > mat_col else "").upper()
    if not material: material = "UNKNOWN MATERIAL"
        
    price = parse_price(row[price_col] if len(row) > price_col else 0)
    
    if price <= 0: return
    
    unique_combinations.add((portal, material))
    if row_date_obj not in aggregated:
        aggregated[row_date_obj] = {"total": 0.0}
        
    aggregated[row_date_obj]["total"] += price
    aggregated[row_date_obj][(portal, material)] = aggregated[row_date_obj].get((portal, material), 0.0) + price


@router.get("/daily-sales")
def daily_sales(date: str = Query(default="today"), current_user=Depends(get_current_user)):
    now = datetime.utcnow()
    aggregated = {}
    unique_combinations = set()
    
    data = fetch_sheet_csv("ORDERS")
    if data and len(data) > 1:
        for row in data[1:]: process_row_for_breakdown(row, 'ORDERS', aggregated, unique_combinations, date, now)
        
    carpet_data = fetch_carpet_sheet_csv()
    if carpet_data and len(carpet_data) > 1:
        for row in carpet_data[1:]: process_row_for_breakdown(row, 'CARPET', aggregated, unique_combinations, date, now)
        
    mkm_data = fetch_mkm_orders_sheet_csv()
    if mkm_data and len(mkm_data) > 1:
        for row in mkm_data[1:]: process_row_for_breakdown(row, 'MKM', aggregated, unique_combinations, date, now)

    if not aggregated:
        return {"headers": [], "sub_headers": [], "rows": [], "total_rows": 0}

    sorted_combos = sorted(list(unique_combinations), key=lambda x: (x[0], x[1]))
    headers = ["", "HG TOTAL"]
    sub_headers = ["", ""]
    
    for combo in sorted_combos:
        headers.append(combo[0])
        sub_headers.append(combo[1])
        
    sorted_dates = sorted(aggregated.keys(), reverse=True)
    rows = []
    for d in sorted_dates:
        row_arr = [d.strftime("%d-%b-%Y"), round(aggregated[d]["total"], 2)]
        for combo in sorted_combos:
            row_arr.append(round(aggregated[d].get(combo, 0.0), 2))
        rows.append(row_arr)
        
    return {
        "headers": headers,
        "sub_headers": sub_headers,
        "rows": rows,
        "total_rows": len(rows)
    }
"""

# Regex to find everything from @router.get("/daily-sales") to @router.get("/daily-sales-items")
pattern = re.compile(r'@router\.get\("/daily-sales"\).*?(?=@router\.get\("/daily-sales-items"\))', re.DOTALL)

if pattern.search(code):
    new_code = pattern.sub(new_func + '\n', code)
    with open('backend/routers/breakdown.py', 'w', encoding='utf-8') as f:
        f.write(new_code)
    print("Successfully replaced daily_sales logic!")
else:
    print("Could not find daily_sales function to replace.")
