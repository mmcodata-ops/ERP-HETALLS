import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure counts contains month and year
content = content.replace('counts = {"today": {}}', 'counts = {"today": {}, "month": {}, "year": {}}')

# Add increments for month and year inside companies_revenue
# In companies_revenue, the logic looks like:
#                 portals["today"][portal] = portals["today"].get(portal, 0) + price
#                 counts["today"][portal] = counts["today"].get(portal, 0) + 1
#             if dt.year == current_year and dt.month == current_month:
#                 portals["month"][portal] = portals["month"].get(portal, 0) + price
#             if fy_start.date() <= dt <= fy_end.date():
#                 portals["year"][portal] = portals["year"].get(portal, 0) + price

content = content.replace('portals["month"][portal] = portals["month"].get(portal, 0) + price',
                          'portals["month"][portal] = portals["month"].get(portal, 0) + price\n                counts["month"][portal] = counts["month"].get(portal, 0) + 1')

content = content.replace('portals["year"][portal] = portals["year"].get(portal, 0) + price',
                          'portals["year"][portal] = portals["year"].get(portal, 0) + price\n                counts["year"][portal] = counts["year"].get(portal, 0) + 1')

# Then when building the item
content = content.replace('''            if key == "today":
                item["order_count"] = counts["today"].get(portal, 0)''',
'''            item["order_count"] = counts[key].get(portal, 0) if key in counts else 0''')

# But wait, we need to be careful with string matching
