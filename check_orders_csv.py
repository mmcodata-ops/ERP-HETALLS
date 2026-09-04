import requests
import csv
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/pub?output=csv"
res = requests.get(url)
reader = csv.reader(res.text.splitlines())
for i, row in enumerate(reader):
    if len(row) > 8 and row[8].strip() and i > 0:
        print(f"ORDERS Row {i+1}: Date='{row[8]}'")
