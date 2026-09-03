import requests, re

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/htmlview'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
# Find the sheet names and GIDs. They usually appear in a JS object or list items.
# Let's search for "name":"Month-Year" and "gid":"..."
matches = re.findall(r'\{[^{]*"name":"([^"]+)"[^{]*"gid":"(\d+)"', r.text)
if matches:
    print("Found via JSON structure:")
    for name, gid in matches:
        print(f"  {name}: {gid}")
else:
    # try another pattern
    html_matches = re.findall(r'id="sheet-button-(\d+)".*?>([^<]+)<', r.text)
    print("Found via HTML buttons:")
    for gid, name in html_matches:
        print(f"  {name}: {gid}")
