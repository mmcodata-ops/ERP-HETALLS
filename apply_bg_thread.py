import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Make CACHE_TTL huge
content = re.sub(r'CACHE_TTL = 10.*?$', 'CACHE_TTL = 86400 # 24 hours (background thread handles updates)', content, flags=re.MULTILINE)

# Add force to fetch_sheet_csv
content = content.replace('def fetch_sheet_csv(sheet_name):', 'def fetch_sheet_csv(sheet_name, force=False):')
content = content.replace('if sheet_name in _CACHE:', 'if not force and sheet_name in _CACHE:')

# Add force to fetch_mkm_orders_sheet_csv
content = content.replace('def fetch_mkm_orders_sheet_csv():', 'def fetch_mkm_orders_sheet_csv(force=False):')
content = content.replace('if sheet_name in _CACHE:', 'if not force and sheet_name in _CACHE:')

# Add force to fetch_carpet_sheet_csv
content = content.replace('def fetch_carpet_sheet_csv():', 'def fetch_carpet_sheet_csv(force=False):')
content = content.replace('if sheet_name in _CACHE:', 'if not force and sheet_name in _CACHE:')

# Add background thread
bg_thread = '''

# Background thread to keep data fresh instantly
def background_sheet_sync():
    import time
    time.sleep(2) # initial delay
    while True:
        try:
            fetch_sheet_csv("ORDERS", force=True)
            fetch_mkm_orders_sheet_csv(force=True)
            fetch_carpet_sheet_csv(force=True)
        except Exception as e:
            print("Background sync error:", e)
        time.sleep(15) # Refresh exactly every 15 seconds!

import threading
threading.Thread(target=background_sheet_sync, daemon=True).start()
'''

content += bg_thread

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
