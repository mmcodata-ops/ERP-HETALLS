import requests, re, json

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/edit'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
text = r.text

# Look for patterns like ["May-2026", 123456789] or similar in the JS
# Often it's something like ["April-2026",1] where 1 is not gid.
# Let's just find all large numbers in the document and try them.
# Wait, let's use the export format without gid and see what it does.
# No, it exports the first tab.

# Let's find all occurrences of "April-2026" and print 500 chars around them to see the JSON
for month in ['April-2026', 'May-2026']:
    for m in re.finditer(month, text):
        start = max(0, m.start() - 200)
        end = min(len(text), m.end() + 200)
        snippet = text[start:end]
        if 'docs-sheet-tab' not in snippet:
            print(f"\n--- JS snippet for {month} ---")
            print(snippet)
