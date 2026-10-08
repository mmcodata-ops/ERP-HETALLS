import os
import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make group_by day and mtd completely identical and foolproof
# We replace the entire dt processing block for all 4 datasets
pattern = r'(if dt:\s*)(if group_by == "mtd" and dt\.day > now\.day:\s*continue\s*)(if group_by == "day":\s*if dt\.day > now\.day: continue\s*label = dt\.strftime\("%b %Y"\)\s*sort_dt = dt\.replace\(day=1, hour=0, minute=0, second=0, microsecond=0\)\s*elif group_by == "week":\s*start_of_week = dt - timedelta\(days=dt\.weekday\(\)\)\s*end_of_week = start_of_week \+ timedelta\(days=6\)\s*label = start_of_week\.strftime\("%b %d"\) \+ " - " \+ end_of_week\.strftime\("%b %d, %Y"\)\s*sort_dt = start_of_week\.replace\(hour=0, minute=0, second=0, microsecond=0\)\s*else:\s*label = dt\.strftime\("%b %Y"\)\s*sort_dt = dt\.replace\(day=1, hour=0, minute=0, second=0, microsecond=0\))'

replacement = r'''\1if group_by in ["day", "mtd"] and dt.day > now.day:
                  continue
              
              if group_by in ["day", "mtd"]:
                  label = dt.strftime("%b %Y")
                  sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
              elif group_by == "week":
                  start_of_week = dt - timedelta(days=dt.weekday())
                  end_of_week = start_of_week + timedelta(days=6)
                  label = start_of_week.strftime("%b %d") + " - " + end_of_week.strftime("%b %d, %Y")
                  sort_dt = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
              else:
                  label = dt.strftime("%b %Y")
                  sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)'''

content = re.sub(pattern, replacement, content)

# Also fix the fy_start filter which missed "day"
content = content.replace('if group_by in ["month", "mtd"] and m["_dt"] < fy_start:', 'if group_by in ["month", "mtd", "day"] and m["_dt"] < fy_start:')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Backend updated.")
