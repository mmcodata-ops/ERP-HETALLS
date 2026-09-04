import urllib.request
import re
url = "https://docs.google.com/spreadsheets/d/1NZo52WV0ynaYe-G2WrZ5ItRwPmNKjdwhr_GOyztAz8U/edit"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
matches = re.findall(r'\[(\d+),\s*"([^"]+)"', html)
for m in matches:
    if "Sales Order" in m[1] or "Stock Details" in m[1] or "ORDERS" in m[1].upper() or "MKM" in m[1].upper():
        print(m[1], ":", m[0])
