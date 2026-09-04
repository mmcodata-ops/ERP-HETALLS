import requests
import csv
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?output=csv"
res = requests.get(url)
rows = list(csv.reader(res.text.splitlines()))
for row in rows[-5:]:
    print(len(row), row[:2] if len(row) > 2 else row)
