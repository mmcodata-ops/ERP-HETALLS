import urllib.request
import re

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/htmlview'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        # Look for sheet metadata in the JS objects
        sheets = re.findall(r'\{[^\}]*"name":"([^"]+)"[^\}]*"gid":"(\d+)"[^\}]*\}', html)
        if not sheets:
             sheets = re.findall(r'"gid":"(\d+)","name":"([^"]+)"', html)
        print('Found sheets:')
        for s in set(sheets):
            print(s)
except Exception as e:
    print('Error:', e)
