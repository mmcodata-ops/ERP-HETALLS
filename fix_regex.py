import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

bad_block = """        if dt:
            if group_by in ["day", "mtd"] and dt.day > now.day:
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
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""

good_block = """        if dt:
            if group_by in ["day", "mtd"] and dt.day > now.day:
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
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""

content = content.replace(bad_block, good_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
