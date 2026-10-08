import os

def revert_backend(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert the label grouping
    wrong_grouping = """            if group_by == "day":
                label = dt.strftime("%b %d")
                sort_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
            elif group_by == "mtd":
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""
    correct_grouping = """            if group_by in ["day", "mtd"]:
                label = dt.strftime("%b %Y")
                sort_dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)"""
    content = content.replace(wrong_grouping, correct_grouping)

    # Revert the condition
    content = content.replace(
        'if group_by == "mtd" and dt.day > now.day:',
        'if group_by in ["day", "mtd"] and dt.day > now.day:'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def revert_frontend(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("revenueChartDay", "revenueChartMtd")
    content = content.replace("setRevenueChartDay", "setRevenueChartMtd")
    
    content = content.replace("group_by=day", "group_by=mtd")
    content = content.replace("rDay", "rMtd")
    
    content = content.replace("chartGroupBy === 'day'", "chartGroupBy === 'mtd'")
    content = content.replace("setChartGroupBy('day')", "setChartGroupBy('mtd')")
    content = content.replace("chartGroupByRef.current = 'day'", "chartGroupByRef.current = 'mtd'")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


revert_backend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP\backend\routers\dashboard.py")
revert_backend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP(1)-SAMPLE\RugsCo_ERP\backend\routers\dashboard.py")

revert_frontend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP\frontend\src\pages\Dashboard.jsx")
revert_frontend(r"Q:\BACK OFFICE\SAHIL\RugsCo_ERP(1)-SAMPLE\RugsCo_ERP\frontend\src\pages\Dashboard.jsx")

print("Reverted to MTD logic successfully!")
