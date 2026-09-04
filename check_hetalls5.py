import requests

# Try export format (works when sheet is shared as Viewer)
url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/export?format=csv&gid=14872727'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
print(f'export status: {r.status_code}')
print(f'Content-Type: {r.headers.get("Content-Type","")}')
if 'csv' in r.headers.get('Content-Type','') or 'text/plain' in r.headers.get('Content-Type',''):
    print(r.text[:500])
else:
    print(r.text[:200])

# Also try gsheet pub with /d/e/ format
url2 = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/gviz/tq?tqx=out:csv&gid=14872727'
r2 = requests.get(url2, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
print(f'\ngviz status: {r2.status_code}')
print(f'Content-Type: {r2.headers.get("Content-Type","")}')
if r2.status_code == 200 and 'html' not in r2.headers.get('Content-Type',''):
    print(r2.text[:500])
