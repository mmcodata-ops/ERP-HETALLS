import requests, csv, io

BASE = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM'

for gid, name in [('528257396', 'August?'), ('14872727', 'September?')]:
    url = f'{BASE}/export?format=csv&gid={gid}'
    r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
    if 'csv' in r.headers.get('Content-Type',''):
        reader = csv.reader(io.StringIO(r.text))
        rows = list(reader)
        dates = [rows[i][8] for i in range(1, min(3, len(rows))) if len(rows[i]) > 8]
        print(f'GID {gid} ({name}): {len(rows)} rows, first dates: {dates}')
