import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("k !== 'order_count'", "k !== 'order_count' && k !== 'order_count_hg' && k !== 'order_count_ho'")
content = content.replace('key !== "order_count"', 'key !== "order_count" && key !== "order_count_hg" && key !== "order_count_ho"')

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
