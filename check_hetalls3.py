import requests

# Try the pub URL with gid for September-2026
url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/pub?output=csv&gid=14872727'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
print(f'Status: {r.status_code}')
print(f'Content-Type: {r.headers.get("Content-Type", "?")}')
print(f'First 500 chars: {r.text[:500]}')
