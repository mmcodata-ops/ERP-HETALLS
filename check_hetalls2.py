import requests

# Try to get the HTML page to find all tab GIDs
url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/pubhtml'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
print(f'Status: {r.status_code}')
print(f'Length: {len(r.text)}')

# Check if it's a login page or actual content
if 'gid=' in r.text:
    import re
    gids = re.findall(r'gid=(\d+)', r.text)
    print(f'Found GIDs: {set(gids)}')

# Also check for tab names
if 'sheet-button' in r.text.lower() or 'tab' in r.text.lower():
    import re
    tabs = re.findall(r'>([^<]*(?:2026|2027)[^<]*)<', r.text)
    print(f'Tab names: {tabs}')
