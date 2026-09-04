with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

bad_line = '            counts["total"][portal] = counts["total"].get(portal, 0) + 1\n'
content = content.replace(bad_line, '')

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
