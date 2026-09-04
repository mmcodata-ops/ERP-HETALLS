import requests
import csv
from datetime import datetime
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
res = requests.get(url)
reader = csv.reader(res.text.splitlines())
for i, row in enumerate(reader):
    if len(row) > 8 and i > 0:
        d = row[8]
        if '2026' in d or '26' in d:
            print(f"[{i+1}] Raw: '{d}'")
