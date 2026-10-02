from fastapi import APIRouter, Depends, Query
import urllib.request
import urllib.parse
import csv
from io import StringIO
from datetime import datetime
from auth import get_current_user
import time
import threading
from routers.dashboard import fetch_carpet_sheet_csv, fetch_mkm_orders_sheet_csv, normalize_portal

router = APIRouter(prefix="/api/breakdown", tags=["breakdown"])

# NOTE: The sheet MUST be "Anyone with the link can view" for this to work!
SHEET_URL_TEMPLATE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?gid=978055065&single=true&output=csv"

_CACHE = {}
_CACHE_LOCK = threading.Lock()
_FETCHING = set()
CACHE_TTL = 10 # 10 seconds for near-live data

def _fetch_from_google(sheet_name):
    if "{}" in SHEET_URL_TEMPLATE:
        url = SHEET_URL_TEMPLATE.format(urllib.parse.quote(sheet_name))
    else:
        url = SHEET_URL_TEMPLATE
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            data = list(csv.reader(StringIO(content)))
            with _CACHE_LOCK:
                _CACHE[sheet_name] = (time.time(), data)
            return data
    except Exception as e:
        print(f"Error fetching sheet {sheet_name}: {e}")
        return None
    finally:
        with _CACHE_LOCK:
            if sheet_name in _FETCHING:
                _FETCHING.remove(sheet_name)

def _bg_fetch(sheet_name):
    with _CACHE_LOCK:
        if sheet_name in _FETCHING:
            return
        _FETCHING.add(sheet_name)
    _fetch_from_google(sheet_name)

def fetch_sheet_csv(sheet_name):
    now = time.time()
    with _CACHE_LOCK:
        if sheet_name in _CACHE:
            cached_time, data = _CACHE[sheet_name]
            if now - cached_time > CACHE_TTL:
                threading.Thread(target=_bg_fetch, args=(sheet_name,)).start()
            return data

    with _CACHE_LOCK:
        _FETCHING.add(sheet_name)
    data = _fetch_from_google(sheet_name)
    return data or []

def parse_price(val_str):
    try:
        if not val_str: return 0.0
        return float(val_str.replace(',', '').replace('$', '').strip())
    except ValueError:
        return 0.0

def parse_date(date_str):
    try:
        if not date_str: return None
        return datetime.strptime(date_str.strip(), "%d-%b-%Y")
    except ValueError:
        return None


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

