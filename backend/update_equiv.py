import re

file_path = 'backend/routers/dashboard.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the equiv logic block
equiv_logic_hg = """            if label not in monthly_data:
                monthly_data[label] = {"month": label, "_dt": sort_dt, "order_count_hg": 0, "order_count_ho": 0, "equiv": {"order_count_hg": 0, "order_count_ho": 0}}
            monthly_data[label][portal] = monthly_data[label].get(portal, 0) + price
            monthly_data[label]["order_count_hg"] += 1
            
            # Equivalent MTD/WTD logic
            is_equiv = False
            if group_by == "month":
                is_equiv = dt.day <= now.day
            elif group_by == "week":
                is_equiv = dt.weekday() <= now.weekday()
            elif group_by == "day":
                is_equiv = True
                
            if is_equiv:
                monthly_data[label]["equiv"][portal] = monthly_data[label]["equiv"].get(portal, 0) + price
                monthly_data[label]["equiv"]["order_count_hg"] += 1"""

target_hg = """            if label not in monthly_data:
                monthly_data[label] = {"month": label, "_dt": sort_dt, "order_count_hg": 0, "order_count_ho": 0}
            monthly_data[label][portal] = monthly_data[label].get(portal, 0) + price
            monthly_data[label]["order_count_hg"] += 1"""
content = content.replace(target_hg, equiv_logic_hg)

equiv_logic_ho = """            if label not in monthly_data:
                monthly_data[label] = {"month": label, "_dt": sort_dt, "order_count_hg": 0, "order_count_ho": 0, "equiv": {"order_count_hg": 0, "order_count_ho": 0}}
            monthly_data[label][portal] = monthly_data[label].get(portal, 0) + price
            monthly_data[label]["order_count_ho"] += 1
            
            # Equivalent MTD/WTD logic
            is_equiv = False
            if group_by == "month":
                is_equiv = dt.day <= now.day
            elif group_by == "week":
                is_equiv = dt.weekday() <= now.weekday()
            elif group_by == "day":
                is_equiv = True
                
            if is_equiv:
                monthly_data[label]["equiv"][portal] = monthly_data[label]["equiv"].get(portal, 0) + price
                monthly_data[label]["equiv"]["order_count_ho"] += 1"""

target_ho = """            if label not in monthly_data:
                monthly_data[label] = {"month": label, "_dt": sort_dt, "order_count_hg": 0, "order_count_ho": 0}
            monthly_data[label][portal] = monthly_data[label].get(portal, 0) + price
            monthly_data[label]["order_count_ho"] += 1"""
content = content.replace(target_ho, equiv_logic_ho)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Backend updated with equiv logic")
