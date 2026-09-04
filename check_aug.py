import csv
with open('mkm_jan2026.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # header
    count = 0
    for row in reader:
        if len(row) > 8 and 'aug' in row[8].lower() and '24' in row[8]:
            count += 1
            print(row[8], row[4], row[6], row[26])
    print(f"Found {count} orders on Aug 24")
