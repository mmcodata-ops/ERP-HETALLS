import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the "day" grouping logic to act as MTD
target_day1 = """            if group_by == "day":
                label = dt.strftime("%b %d, %Y")
                sort_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)"""
replacement_day1 = """            if group_by == "day":
                if dt.day > now.day: continue
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""
content = content.replace(target_day1, replacement_day1)

# Remove the [-30:] slicing for "day", and make it obey fy_start like "month" does.
target_slice = """    # Filter by group_by (don't show 52 weeks if not needed)
    if group_by == "week":
        sorted_months = sorted_months[-16:] # Last 16 weeks max for readability
    elif group_by == "day":
        sorted_months = sorted_months[-30:] # Last 30 days
        
    for m in sorted_months:
        if group_by == "month" and m["_dt"] < fy_start:
            continue"""

replacement_slice = """    # Filter by group_by (don't show 52 weeks if not needed)
    if group_by == "week":
        sorted_months = sorted_months[-16:] # Last 16 weeks max for readability
        
    for m in sorted_months:
        if group_by in ("month", "day") and m["_dt"] < fy_start:
            continue"""
content = content.replace(target_slice, replacement_slice)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Backend updated: Date view is now MTD")
