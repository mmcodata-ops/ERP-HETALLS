import requests, re, json

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/edit'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
# Google injects a script tag: window.bootstrapData = ...
match = re.search(r'var bootstrapData = (\{.*?\});', r.text)
if not match:
    match = re.search(r'window\["waffle\.config\.fb_data"\] = (\[.*?\]);', r.text)

# Let's just blindly regex for names that look like months and adjacent GIDs
# A common structure is ["Sheet Name", gid] or something similar
tabs = re.findall(r'\["([A-Za-z]+[- ]202[0-9])",(\d+)\]', r.text)
if tabs:
    print("Found tabs (pattern 1):")
    for name, gid in set(tabs):
        print(f"  {name}: {gid}")
else:
    tabs = re.findall(r'\["([A-Za-z]+[- ]202[0-9])"[^\]]*?(\d{5,12})', r.text)
    if tabs:
        print("Found tabs (pattern 2):")
        for name, gid in set(tabs):
            print(f"  {name}: {gid}")
    else:
        # just print all strings that look like a month-year
        months = re.findall(r'[A-Za-z]+-202[0-9]', r.text)
        print("Raw month strings:", set(months))
        # look for gids
        gids = re.findall(r'gid=(\d+)', r.text)
        print("Raw GIDs:", set(gids))
