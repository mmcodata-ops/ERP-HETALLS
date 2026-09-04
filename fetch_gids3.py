import requests, re

url = 'https://docs.google.com/spreadsheets/d/1JBOBE5pkjbKMv3F8dIXIDPBI7jKXxduTjKWDQz4VrGM/edit'
r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
text = r.text

for month in ['April-2026', 'May-2026', 'June-2026', 'July-2026', 'August-2026', 'September-2026']:
    # Find the index of the month name
    idx = text.find(month)
    if idx != -1:
        # Extract a window around it
        window = text[max(0, idx-50):min(len(text), idx+100)]
        print(f"\n--- {month} ---")
        print(window)
        # Try to find a long number nearby
        numbers = re.findall(r'\b\d{6,12}\b', window)
        print("Nearby numbers:", numbers)
