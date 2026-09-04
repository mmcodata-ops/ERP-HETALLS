import re

with open('dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_func = '''def fetch_mkm_orders_sheet_csv():
    now = time.time()
    sheet_name = "MKM_ORDERS"
    with _CACHE_LOCK:
        if sheet_name in _CACHE:
            cached_time, data = _CACHE[sheet_name]
            if now - cached_time <= CACHE_TTL:
                return data
                
        if sheet_name in _FETCH_EVENTS:
            event = _FETCH_EVENTS[sheet_name]
            needs_fetch = False
        else:
            event = threading.Event()
            _FETCH_EVENTS[sheet_name] = event
            needs_fetch = True

    if needs_fetch:
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            csv_data = response.read().decode('utf-8')
            reader = csv.reader(csv_data.splitlines())
            data = list(reader)
        except Exception as e:
            print(f"Error fetching MKM orders sheet: {e}")
            data = None
            
        with _CACHE_LOCK:
            if data is not None:
                _CACHE[sheet_name] = (time.time(), data)
            del _FETCH_EVENTS[sheet_name]
        event.set()
    else:
        event.wait()
        
    with _CACHE_LOCK:
        if sheet_name in _CACHE:
            return _CACHE[sheet_name][1]
        return []
'''

old_func_regex = r"def fetch_mkm_orders_sheet_csv\(\).*?return data\n"

content = re.sub(old_func_regex, new_func, content, flags=re.DOTALL)

with open('dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
