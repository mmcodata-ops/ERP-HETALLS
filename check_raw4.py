import requests
import csv
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?output=csv"
res = requests.get(url)
rows = list(csv.reader(res.text.splitlines()))
for i, row in enumerate(rows[-15:]):
    if len(row) > 36:
        print(f"Date='{row[8]}' Price='{row[36]}'")
