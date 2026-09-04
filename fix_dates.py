with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pattern = r'    formats = \[\n.*?\]\n'

new_formats = '''    formats = [
        "%d-%b-%Y", "%d-%b-%y", "%d %b %Y", "%d %b %y",
        "%b %d, %Y", "%b %d %Y", "%d-%B-%Y", "%d %B %Y",
        "%B %d, %Y", "%B %d %Y", "%d/%m/%Y", "%m/%d/%Y",
        "%d/%m/%y", "%m/%d/%y", "%d-%m-%Y", "%m-%d-%Y",
        "%d-%m-%y", "%m-%d-%y", "%Y-%m-%d", "%Y/%m/%d"
    ]
'''

content = re.sub(pattern, new_formats, content, flags=re.DOTALL)

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
