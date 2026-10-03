lines = []
with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    for line in f:
        if 'counts = {"today": {}}' in line:
            line = line.replace('counts = {"today": {}}', 'counts = {"today": {}, "month": {}, "year": {}}')
            
        if 'portals["month"][portal] = portals["month"].get(portal, 0) + price' in line:
            lines.append(line)
            # Find indentation
            indent = line[:len(line) - len(line.lstrip())]
            lines.append(indent + 'counts["month"][portal] = counts["month"].get(portal, 0) + 1\n')
            continue
            
        if 'portals["year"][portal] = portals["year"].get(portal, 0) + price' in line:
            lines.append(line)
            indent = line[:len(line) - len(line.lstrip())]
            lines.append(indent + 'counts["year"][portal] = counts["year"].get(portal, 0) + 1\n')
            continue
            
        if 'if key == "today":' in line:
            # We want to change the next line
            pass
        elif 'item["order_count"] = counts["today"].get(portal, 0)' in line:
            line = line.replace('counts["today"].get(portal, 0)', 'counts.get(key, {}).get(portal, 0)')
            lines.append(line)
            continue
            
        lines.append(line)

# Remove the 'if key == "today":' entirely?
# Actually, if I just replaced the line inside the if block, it only assigns for "today".
# Let's fix that.
