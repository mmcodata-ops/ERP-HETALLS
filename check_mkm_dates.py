import requests
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTiemI7xv-XbL0WHtwPU4lsTpC1Xnssb8SKAYZHfVhjZqOjUinM59FxJRBLEd8_aghEbFxZhoKz-MQa/pub?output=csv&gid=277725317"
res = requests.get(url)
lines = res.text.splitlines()
for i, line in enumerate(lines):
    row = line.split(',')
    if len(row) > 8:
        print(f"Row {i+1}: {row[8]}")
