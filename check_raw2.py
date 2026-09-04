import requests
import csv
from datetime import datetime
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?output=csv"
res = requests.get(url)
reader = csv.reader(res.text.splitlines())
for i, row in enumerate(reader):
    if len(row) > 8 and i > 0:
        d = row[8]
        if 'Aug' in d or 'aug' in d.lower() or '/08/' in d or '-08-' in d:
            print(f"[{i+1}] Raw: '{d}'")
