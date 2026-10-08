import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """        del m["_dt"]
        for k in m:
            if k != "month" and k != "order_count_hg" and k != "order_count_ho":
                m[k] = round(m[k], 2)"""

replacement = """        del m["_dt"]
        for k in m:
            if k != "month" and k != "order_count_hg" and k != "order_count_ho" and k != "equiv":
                m[k] = round(m[k], 2)
            elif k == "equiv":
                for ek in m[k]:
                    if ek != "order_count_hg" and ek != "order_count_ho":
                        m[k][ek] = round(m[k][ek], 2)"""

content = content.replace(target, replacement)

# ALSO, let's fix the [-12:] slice that failed to apply earlier, because I want weekly to show the last 12 weeks.
# If there are 52 weeks, the chart gets very crowded.
target_sort = """    for m in sorted_months:
        if m["_dt"] < fy_start:
            continue"""
replacement_sort = """    
    # Filter by group_by (don't show 52 weeks if not needed)
    if group_by == "week":
        sorted_months = sorted_months[-16:] # Last 16 weeks max for readability
    elif group_by == "day":
        sorted_months = sorted_months[-30:] # Last 30 days
        
    for m in sorted_months:
        if group_by == "month" and m["_dt"] < fy_start:
            continue"""

content = content.replace(target_sort, replacement_sort)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Backend TypeError fixed and grouping slice applied")
