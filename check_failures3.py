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

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTRxG5U4P6Bq8x4G-qM2Ff3_K8Pz44L9GZ6B_m7K2b8X6q4Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z7Z/pub?output=csv&gid=1394514115"
res = requests.get(url)
if res.status_code == 200:
    reader = csv.reader(res.text.splitlines())
    failed = 0
    for i, row in enumerate(reader):
        if len(row) > 8 and i > 0:
            d = row[8]
            if d.strip() and not parse_date(d):
                print(f"FAILED CARPET: '{d}'")
                failed += 1
    print(f"Total CARPET Failed: {failed}")
