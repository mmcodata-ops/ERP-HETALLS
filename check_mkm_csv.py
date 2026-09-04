import requests
import csv
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
res = requests.get(url)
reader = csv.reader(res.text.splitlines())
for i, row in enumerate(reader):
    if len(row) > 26 and row[26].strip():
        print(f"Row {i+1}: Date='{row[8]}' Price='{row[26]}'")
