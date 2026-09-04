import re

with open('dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_func = '''def fetch_mkm_orders_sheet_csv():
    now = time.time()
    sheet_name = "MKM_ORDERS"
    
    with _FETCHING_LOCKS[sheet_name]:
        if sheet_name in _CACHE and (now - _CACHE[sheet_name][0]) < CACHE_TTL:
            return _CACHE[sheet_name][1]
        
        _FETCH_EVENTS[sheet_name].clear()
        
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            csv_data = response.read().decode('utf-8')
            reader = csv.reader(csv_data.splitlines())
            data = list(reader)
            _CACHE[sheet_name] = (now, data)
        except Exception as e:
            print(f"Error fetching MKM orders sheet: {e}")
            if sheet_name in _CACHE:
                data = _CACHE[sheet_name][1]
            else:
                data = []
                
        _FETCH_EVENTS[sheet_name].set()
        return data
'''

old_func = '''def fetch_mkm_orders_sheet_csv():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
    try:
        response = urllib.request.urlopen(url)
        csv_data = response.read().decode('utf-8')
        reader = csv.reader(csv_data.splitlines())
        return list(reader)
    except Exception as e:
        print(f"Error fetching MKM orders sheet: {e}")
        return []'''

if old_func in content:
    content = content.replace(old_func, new_func)
else:
    print("Could not find old func")

with open('dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)

