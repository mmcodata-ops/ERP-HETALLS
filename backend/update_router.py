import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure Query is imported
if 'from fastapi import APIRouter, Depends, Query' not in content and 'from fastapi import APIRouter, Depends, HTTPException, Query' not in content:
    content = content.replace('from fastapi import APIRouter, Depends, HTTPException', 'from fastapi import APIRouter, Depends, HTTPException, Query')
    content = content.replace('from fastapi import APIRouter, Depends', 'from fastapi import APIRouter, Depends, Query')

# Replace the revenue-chart endpoint definition
target = """@router.get("/revenue-chart")
def revenue_chart(current_user=Depends(get_current_user)):
    now = datetime.now()"""

replacement = """@router.get("/revenue-chart")
def revenue_chart(group_by: str = "month", current_user=Depends(get_current_user)):
    now = datetime.now()"""
content = content.replace(target, replacement)

# Replace the label logic for HG orders
target_hg = """        if dt:
            month_label = dt.strftime("%b %Y")
            if month_label not in monthly_data:
                monthly_data[month_label] = {"month": month_label, "_dt": dt.replace(day=1), "order_count_hg": 0, "order_count_ho": 0}
            monthly_data[month_label][portal] = monthly_data[month_label].get(portal, 0) + price
            monthly_data[month_label]["order_count_hg"] += 1"""

replacement_hg = """        if dt:
            if group_by == "day":
                label = dt.strftime("%b %d, %Y")
                sort_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
            elif group_by == "week":
                start_of_week = dt - timedelta(days=dt.weekday())
                end_of_week = start_of_week + timedelta(days=6)
                label = start_of_week.strftime("%b %d") + " - " + end_of_week.strftime("%b %d, %Y")
                sort_dt = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                
            if label not in monthly_data:
                monthly_data[label] = {"month": label, "_dt": sort_dt, "order_count_hg": 0, "order_count_ho": 0}
            monthly_data[label][portal] = monthly_data[label].get(portal, 0) + price
            monthly_data[label]["order_count_hg"] += 1"""
content = content.replace(target_hg, replacement_hg)

# Replace the label logic for HO (carpet) orders
target_ho = """        if dt:
            month_label = dt.strftime("%b %Y")
            if month_label not in monthly_data:
                monthly_data[month_label] = {"month": month_label, "_dt": dt.replace(day=1), "order_count_hg": 0, "order_count_ho": 0}
            monthly_data[month_label][portal] = monthly_data[month_label].get(portal, 0) + price
            monthly_data[month_label]["order_count_ho"] += 1"""

replacement_ho = """        if dt:
            if group_by == "day":
                label = dt.strftime("%b %d, %Y")
                sort_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
            elif group_by == "week":
                start_of_week = dt - timedelta(days=dt.weekday())
                end_of_week = start_of_week + timedelta(days=6)
                label = start_of_week.strftime("%b %d") + " - " + end_of_week.strftime("%b %d, %Y")
                sort_dt = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                
            if label not in monthly_data:
                monthly_data[label] = {"month": label, "_dt": sort_dt, "order_count_hg": 0, "order_count_ho": 0}
            monthly_data[label][portal] = monthly_data[label].get(portal, 0) + price
            monthly_data[label]["order_count_ho"] += 1"""
content = content.replace(target_ho, replacement_ho)

# Add logic to slice the last 30 days or 12 weeks so the chart isn't unreadable, 
# But only if it's day/week. For month, we keep all.
# Actually, the sorting happens at the end:
# results = sorted(list(monthly_data.values()), key=lambda x: x["_dt"])
# We can slice it there.
target_sort = "results = sorted(list(monthly_data.values()), key=lambda x: x[\"_dt\"])"
replacement_sort = """results = sorted(list(monthly_data.values()), key=lambda x: x["_dt"])
    if group_by == "day":
        results = results[-30:] # Last 30 days
    elif group_by == "week":
        results = results[-12:] # Last 12 weeks"""
content = content.replace(target_sort, replacement_sort)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Backend updated.")
