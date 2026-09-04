import requests, csv, io, re

BASE = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM'

# Get the HTML page to find all tab GIDs
r = requests.get(f'{BASE}/edit', timeout=15, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
gids = set(re.findall(r'gid[=:](\d+)', r.text))
print(f'Found GIDs from HTML: {gids}')

# Also try pubhtml
r2 = requests.get(f'{BASE}/pubhtml', timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
if r2.status_code == 200:
    gids2 = set(re.findall(r'gid=(\d+)', r2.text))
    tabs = re.findall(r'class=\"sheet-menu-button[^\"]*\"[^>]*>([^<]+)', r2.text)
    print(f'pubhtml GIDs: {gids2}')
    print(f'Tab names: {tabs}')

# Print column headers for September
url = f'{BASE}/export?format=csv&gid=14872727'
r3 = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
reader = csv.reader(io.StringIO(r3.text))
rows = list(reader)
print(f'\nSeptember-2026: {len(rows)} rows, {len(rows[0])} cols')
print('Header:')
for i, h in enumerate(rows[0]):
    print(f'  [{i}] {h}')
print('Row 1 sample (key cols):')
if len(rows)>1:
    r = rows[1]
    print(f'  Portal[4]={r[4]}, OrderNo[5]={r[5]}, Buyer[6]={r[6]}, Date[8]={r[8]}, Qty[9]={r[9]}, Item[10]={r[10]}, Size[11]={r[11]}, Status[14]={r[14]}, Price[36]={r[36] if len(r)>36 else "N/A"}')
