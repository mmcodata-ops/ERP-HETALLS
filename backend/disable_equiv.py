import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Disable equiv for month
target = """            is_equiv = False
            if group_by == "month":
                is_equiv = dt.day <= now.day"""
replacement = """            is_equiv = False
            if group_by == "month":
                is_equiv = False # User requested standard raw comparison for Monthly view"""

content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Disabled MTD equiv logic for Monthly view")
