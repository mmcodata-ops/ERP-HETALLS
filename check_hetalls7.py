import requests, re

BASE = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM'

# Try fetching the HTML version to find all sheet GIDs
for endpoint in ['/pubhtml', '/htmlview']:
    r = requests.get(f'{BASE}{endpoint}', timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        gids = re.findall(r'gid=(\d+)', r.text)
        tabs = re.findall(r'>((?:January|February|March|April|May|June|July|August|September|October|November|December)[\-\s]?\d{4})<', r.text, re.IGNORECASE)
        print(f'{endpoint}: status={r.status_code}, gids={set(gids)}, tabs={tabs}')
        
        # Also look for sheet-button patterns
        buttons = re.findall(r'id=\"sheet-button-(\d+)\"[^>]*>([^<]+)', r.text)
        if buttons:
            print(f'Sheet buttons: {buttons}')
