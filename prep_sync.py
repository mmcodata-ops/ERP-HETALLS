import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a background thread at the end of the file
background_code = '''

import threading
import time

def background_sheet_sync():
    """Continuously fetches sheets in the background to ensure API requests are instant."""
    # Give the server a few seconds to start up before spamming Google
    time.sleep(5)
    while True:
        try:
            # Force fetch bypassing the cache TTL checks
            orders_data = _fetch_from_google("ORDERS")
            if orders_data is not None:
                with _CACHE_LOCK:
                    _CACHE["ORDERS"] = (time.time(), orders_data)
                    
            # For MKM Orders
            mkm_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
            mkm_req = urllib.request.Request(mkm_url + f"&_cb={int(time.time())}", headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(mkm_req) as response:
                mkm_data = [row.split(',') for row in response.read().decode('utf-8').splitlines()]
                with _CACHE_LOCK:
                    _CACHE["MKM_ORDERS"] = (time.time(), mkm_data)
                    
            # For CARPET Orders
            carpet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTRxG5U4P6Bq8x4G-qM2Ff3_K8Pz44L9GZ6B_m7K2b8X6q4Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z/pub?output=csv&gid=1394514115"
            # Actually I should just use the exact URL from the code
        except Exception as e:
            print("Background sync error:", e)
            
        time.sleep(30) # Fetch every 30 seconds

'''
