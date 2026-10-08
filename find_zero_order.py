import urllib.request
import csv
import io
import time

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?gid=978055065&single=true&output=csv'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
csv_data = resp.read().decode('utf-8')
reader = list(csv.reader(io.StringIO(csv_data)))

print("Scanning for $0 orders in October 2026...")
found = 0
for i, row in enumerate(reader[1:], start=2):
    if len(row) < 37: continue
    
    status = row[14].strip().lower() if len(row) > 14 else ''
    if status == 'returned': continue
    
    date_str = row[8].strip()
    price_str = row[36].strip()
    
    # parse price
    price = 0.0
    try:
        if price_str:
            clean_str = price_str.replace('$', '').replace(',', '').strip()
            if clean_str:
                price = float(clean_str)
    except:
        price = 0.0

    # Specifically check if date has October and 2026, and price is 0
    # Dates usually look like "2026-10-05" or "10/05/2026"
    if price == 0.0 and '2026' in date_str and ('-10-' in date_str or date_str.startswith('10/')):
        found += 1
        print(f"Row {i} in Google Sheet:")
        print(f"  Order ID:   {row[5]}")
        print(f"  Date:       {date_str}")
        print(f"  Portal:     {row[4]}")
        print(f"  Customer:   {row[6]}")
        print(f"  Product:    {row[10]} {row[11]}")
        print(f"  Status:     {row[14]}")
        print(f"  Raw Price:  '{price_str}'")
        print("-" * 40)

if found == 0:
    print("No $0 orders found in October 2026 in the main ORDERS sheet. Checking CARPET and MKM just in case...")

