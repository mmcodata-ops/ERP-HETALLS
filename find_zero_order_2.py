import urllib.request
import csv
import io

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?gid=978055065&single=true&output=csv'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
csv_data = resp.read().decode('utf-8')
reader = list(csv.reader(io.StringIO(csv_data)))

for i, row in enumerate(reader[1:], start=2):
    if len(row) < 37: continue
    status = row[14].strip().lower() if len(row) > 14 else ''
    if status == 'returned': continue
    date_str = row[8].strip()
    price_str = row[36].strip()
    price = 0.0
    try:
        if price_str:
            clean_str = price_str.replace('$', '').replace(',', '').strip()
            if clean_str: price = float(clean_str)
    except:
        price = 0.0

    if price == 0.0 and '2026' in date_str:
        print(f"Row {i}: Date={date_str}, Portal={row[4]}, ID={row[5]}, Price='{price_str}'")
