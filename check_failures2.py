import requests
import csv
from datetime import datetime
def parse_date(date_str):
    if not date_str: return None
    date_str = date_str.strip()
    formats = [
        "%d-%b-%Y", "%d-%b-%y", "%d %b %Y", "%d %b %y",
        "%b %d, %Y", "%b %d %Y", "%d-%B-%Y", "%d %B %Y",
        "%B %d, %Y", "%B %d %Y", "%d/%m/%Y", "%m/%d/%Y",
        "%d/%m/%y", "%m/%d/%y", "%d-%m-%Y", "%m-%d-%Y",
        "%d-%m-%y", "%m-%d-%y", "%Y-%m-%d", "%Y/%m/%d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    return None

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?output=csv"
res = requests.get(url)
reader = csv.reader(res.text.splitlines())
failed = 0
for i, row in enumerate(reader):
    if len(row) > 8 and i > 0:
        d = row[8]
        if d.strip() and not parse_date(d):
            print(f"FAILED ORDERS: '{d}'")
            failed += 1
print(f"Total ORDERS Failed: {failed}")
