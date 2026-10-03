import sys

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_next = False

for i, line in enumerate(lines):
    if skip_next:
        skip_next = False
        continue
        
    if 'counts = {"today": {}}' in line:
        line = line.replace('counts = {"today": {}}', 'counts = {"today": {}, "month": {}, "year": {}}')
        
    if 'portals["month"][portal] = portals["month"].get(portal, 0) + price' in line:
        new_lines.append(line)
        indent = line[:len(line) - len(line.lstrip())]
        new_lines.append(indent + 'counts["month"][portal] = counts["month"].get(portal, 0) + 1\n')
        continue
        
    if 'portals["year"][portal] = portals["year"].get(portal, 0) + price' in line:
        new_lines.append(line)
        indent = line[:len(line) - len(line.lstrip())]
        new_lines.append(indent + 'counts["year"][portal] = counts["year"].get(portal, 0) + 1\n')
        continue
        
    if 'if key == "today":' in line and 'item["order_count"] =' in lines[i+1]:
        # we want to assign it regardless of key
        indent = line[:len(line) - len(line.lstrip())]
        new_lines.append(indent + 'item["order_count"] = counts.get(key, {}).get(portal, 0)\n')
        skip_next = True
        continue
        
    new_lines.append(line)

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated orders count for all periods")
