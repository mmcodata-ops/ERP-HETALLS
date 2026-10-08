import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for i, line in enumerate(lines):
    # Fix the indentation of the block I inserted
    if "if group_by in [\"day\", \"mtd\"] and dt.day > now.day:" in line:
        line = "            if group_by in [\"day\", \"mtd\"] and dt.day > now.day:\n"
    elif "continue" in line and "group_by in [\"day\", \"mtd\"]" in lines[i-1]:
        line = "                continue\n"
    elif "if group_by in [\"day\", \"mtd\"]:" in line:
        line = "            if group_by in [\"day\", \"mtd\"]:\n"
    elif "label = dt.strftime(\"%b %Y\")" in line and "if group_by in [\"day\", \"mtd\"]:" in lines[i-1]:
        line = "                label = dt.strftime(\"%b %Y\")\n"
    elif "sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)" in line and "label =" in lines[i-1] and "strftime(\"%b" in lines[i-1]:
        line = "                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)\n"
    elif "elif group_by == \"week\":" in line:
        line = "            elif group_by == \"week\":\n"
    elif "start_of_week = dt - timedelta(days=dt.weekday())" in line:
        line = "                start_of_week = dt - timedelta(days=dt.weekday())\n"
    elif "end_of_week = start_of_week + timedelta(days=6)" in line:
        line = "                end_of_week = start_of_week + timedelta(days=6)\n"
    elif "label = start_of_week.strftime(\"%b %d\") + \" - \" + end_of_week.strftime(\"%b %d, %Y\")" in line:
        line = "                label = start_of_week.strftime(\"%b %d\") + \" - \" + end_of_week.strftime(\"%b %d, %Y\")\n"
    elif "sort_dt = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)" in line:
        line = "                sort_dt = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)\n"
    elif "else:" in line and "sort_dt = start_of_week.replace" in lines[i-1]:
        line = "            else:\n"
    out_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(out_lines)
