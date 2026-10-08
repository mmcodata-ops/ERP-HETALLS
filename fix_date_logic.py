import re

def fix_backend(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the `day` and `mtd` grouping condition
    content = content.replace(
        'if group_by in ["day", "mtd"] and dt.day > now.day:',
        'if group_by == "mtd" and dt.day > now.day:'
    )
    
    # 2. Fix the label grouping
    target_grouping = """            if group_by in ["day", "mtd"]:
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""
    
    replacement_grouping = """            if group_by == "day":
                label = dt.strftime("%b %d")
                sort_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
            elif group_by == "mtd":
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""
                
    content = content.replace(target_grouping, replacement_grouping)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def fix_frontend(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace mtd with day in state
    content = content.replace("revenueChartMtd", "revenueChartDay")
    content = content.replace("setRevenueChartMtd", "setRevenueChartDay")
    
    # In Promise.all
    content = content.replace("group_by=mtd", "group_by=day")
    content = content.replace("rMtd", "rDay")
    
    # In chartGroupBy switch
    content = content.replace("chartGroupBy === 'mtd'", "chartGroupBy === 'day'")
    content = content.replace("setChartGroupBy('mtd')", "setChartGroupBy('day')")
    content = content.replace("chartGroupByRef.current = 'mtd'", "chartGroupByRef.current = 'day'")
    content = content.replace("data-v={chartGroupBy}", "data-v={chartGroupBy}") # no change
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_backend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP\backend\routers\dashboard.py")
fix_backend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP(1)-SAMPLE\RugsCo_ERP\backend\routers\dashboard.py")

fix_frontend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP\frontend\src\pages\Dashboard.jsx")
fix_frontend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP(1)-SAMPLE\RugsCo_ERP\frontend\src\pages\Dashboard.jsx")
print("Fixed!")
