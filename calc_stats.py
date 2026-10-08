import sys
sys.path.insert(0, './backend')
import routers.dashboard
from unittest.mock import MagicMock
import json

routers.dashboard.get_current_user = MagicMock(return_value={"id": 1})

print("=== MONTH VIEW ===")
res_month = routers.dashboard.revenue_chart(group_by="month", current_user={"id": 1})
sep_month = next((r for r in res_month if "Sep" in r.get("month")), None)
oct_month = next((r for r in res_month if "Oct" in r.get("month")), None)

print(f"Sep Month Data: {json.dumps(sep_month, indent=2)}")
print(f"Oct Month Data: {json.dumps(oct_month, indent=2)}")


print("\n=== DATE VIEW (MTD) ===")
res_mtd = routers.dashboard.revenue_chart(group_by="mtd", current_user={"id": 1})
sep_mtd = next((r for r in res_mtd if "Sep" in r.get("month")), None)
oct_mtd = next((r for r in res_mtd if "Oct" in r.get("month")), None)

print(f"Sep MTD Data: {json.dumps(sep_mtd, indent=2)}")
print(f"Oct MTD Data: {json.dumps(oct_mtd, indent=2)}")

def calc_pct(current, prev):
    if not prev: return 0
    return ((current - prev) / prev) * 100

if sep_month and oct_month:
    sep_total = sum(v for k,v in sep_month.items() if k not in ['month', 'order_count_hg', 'order_count_ho', 'equiv', '_dt'])
    oct_total = sum(v for k,v in oct_month.items() if k not in ['month', 'order_count_hg', 'order_count_ho', 'equiv', '_dt'])
    print(f"\nMONTH VIEW PERCENTAGE:")
    print(f"Sep Total: {sep_total}")
    print(f"Oct Total: {oct_total}")
    print(f"Percentage: {calc_pct(oct_total, sep_total):.2f}%")

if sep_mtd and oct_mtd:
    sep_total_mtd = sum(v for k,v in sep_mtd.items() if k not in ['month', 'order_count_hg', 'order_count_ho', 'equiv', '_dt'])
    oct_total_mtd = sum(v for k,v in oct_mtd.items() if k not in ['month', 'order_count_hg', 'order_count_ho', 'equiv', '_dt'])
    print(f"\nDATE VIEW (MTD) PERCENTAGE:")
    print(f"Sep MTD Total: {sep_total_mtd}")
    print(f"Oct MTD Total: {oct_total_mtd}")
    print(f"Percentage: {calc_pct(oct_total_mtd, sep_total_mtd):.2f}%")
