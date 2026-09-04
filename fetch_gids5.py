import requests, re

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/edit'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})

# Pattern: [21350203,"[7,0,\"982943342\",[{\"1\":[[0,0,\"May-2026\"]
# We can regex for \"(\d+)\".*?\"([A-Za-z]+[- ]202[0-9])\"
matches = re.findall(r'\\\"(\d+)\\\".*?\\\"([A-Za-z]+[- ]202[0-9])\\\"', r.text)

for gid, name in matches:
    print(f"{name}: {gid}")

