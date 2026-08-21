import re

with open('dashboard.py', 'r') as f:
    content = f.read()

# Replace portal assignment for carpet in companies_revenue, revenue_chart, recent_orders, today_orders
content = content.replace('''portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        price = parse_price(row[18])''', '''portal = (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN"
        portal = f"{portal} (CARPET)"
        price = parse_price(row[18])''')

content = content.replace('''"platform": (row[4].strip() or "UNKNOWN").upper() if len(row) > 4 else "UNKNOWN",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",''', '''"platform": ((row[4].strip() or "UNKNOWN").upper() + " (CARPET)") if len(row) > 4 else "UNKNOWN (CARPET)",
            "customer_name": row[6].strip() if len(row) > 6 else "Unknown",''')

with open('dashboard.py', 'w') as f:
    f.write(content)
