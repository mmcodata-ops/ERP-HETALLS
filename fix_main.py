with open('backend/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('accounts, hr, reports', 'accounts, reports')

with open('backend/main.py', 'w', encoding='utf-8') as f:
    f.write(content)
