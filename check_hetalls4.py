import requests, csv, io

# Try the pub URL again for September-2026 tab
url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/pub?output=csv&gid=14872727'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
print(f'Status: {r.status_code}')
if r.status_code == 200 and 'html' not in r.headers.get('Content-Type',''):
    reader = csv.reader(io.StringIO(r.text))
    rows = list(reader)
    print(f'Total rows: {len(rows)}')
    print(f'Total columns: {len(rows[0])}')
    print('--- HEADER ---')
    for i, col in enumerate(rows[0]):
        print(f'  [{i}] {col}')
    if len(rows) > 1:
        print('--- ROW 1 ---')
        for i, col in enumerate(rows[1]):
            print(f'  [{i}] {col}')
else:
    print(f'Content-Type: {r.headers.get("Content-Type")}')
    print(r.text[:300])
