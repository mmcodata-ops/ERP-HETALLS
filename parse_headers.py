import csv
with open('mkm_jan2026.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for i, h in enumerate(headers):
        print(f"{i}: {h}")
