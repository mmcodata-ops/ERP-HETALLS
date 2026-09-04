import requests, csv, io

# Fetch September-2026 tab to see all columns
url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/export?format=csv&gid=14872727'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
reader = csv.reader(io.StringIO(r.text))
rows = list(reader)
print(f'Total rows: {len(rows)}')
print(f'Total columns: {len(rows[0])}')
print('--- HEADER ---')
for i, col in enumerate(rows[0]):
    print(f'  [{i}] {col}')
print('--- ROW 1 ---')
if len(rows) > 1:
    for i, col in enumerate(rows[1]):
        print(f'  [{i}] {col}')
