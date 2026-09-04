import urllib.request
import re

url = "https://docs.google.com/spreadsheets/d/1NZo52WV0ynaYe-G2WrZ5ItRwPmNKjdwhr_GOyztAz8U/edit"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find something like: [, "Sales Order", 12345678, ...
    matches = re.findall(r'\["[^"]*",\s*"([^"]+)",\s*(\d+)', html)
    for m in matches:
        print(m[0], ":", m[1])
        
    print("\nAlternative regex:")
    matches2 = re.findall(r'\{[^\}]*"name":\s*"([^"]+)"[^\}]*"sheetId":\s*(\d+)', html)
    for m in matches2:
        print(m[0], ":", m[1])
        
    print("\nAlternative 3:")
    matches3 = re.findall(r'\[(\d+),\s*"([^"]+)"', html)
    for m in matches3:
        print(m[1], ":", m[0])
except Exception as e:
    import traceback
    traceback.print_exc()
