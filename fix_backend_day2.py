import os

def fix_backend_day(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    target_grouping = """            if group_by in ["day", "mtd"]:
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""
    
    replacement_grouping = """            if group_by == "mtd":
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            elif group_by == "day":
                label = dt.strftime("%d %b")
                sort_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)"""
                
    content = content.replace(target_grouping, replacement_grouping)
    content = content.replace('if group_by in ["day", "mtd"] and dt.day > now.day:', 'if group_by == "mtd" and dt.day > now.day:')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_backend_day(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP\backend\routers\dashboard.py")
fix_backend_day(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP(1)-SAMPLE\RugsCo_ERP\backend\routers\dashboard.py")
print("Backend fixed for daily data")
