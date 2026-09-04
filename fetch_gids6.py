import requests, re

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/edit'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})

matches = re.findall(r'\\\"(\d+)\\\"\,\[\{\\\"1\\\"\:\[\[0\,0\,\\\"([A-Za-z]+[- ]202[0-9])\\\"', r.text)

for gid, name in matches:
    print(f"{name}: {gid}")
