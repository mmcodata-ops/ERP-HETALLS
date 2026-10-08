import sys
sys.path.insert(0, './backend')
import routers.dashboard
from unittest.mock import MagicMock
import json

routers.dashboard.get_current_user = MagicMock(return_value={"id": 1})

res_month = routers.dashboard.revenue_chart(group_by="month", current_user={"id": 1})
sep_month = next((r for r in res_month if "Sep" in r.get("month")), {})
oct_month = next((r for r in res_month if "Oct" in r.get("month")), {})

def calc_pct(current, prev):
    if not prev: return "+100.00%"
    return f"{((current - prev) / prev) * 100:+.2f}%"

def filter_hg(data):
    return {k: v for k, v in data.items() if "HETALLS" not in k and k not in ['month', 'order_count_hg', 'order_count_ho', 'equiv', '_dt', 'EBAY-RUGSFOREVER', 'PEPPERFRY', 'JAYPOR', 'WALMART']}

oct_keys = filter_hg(oct_month).keys()

print("PORTAL BREAKDOWN (Month View)\n")
for k in oct_keys:
    oct_val = oct_month.get(k, 0)
    sep_val = sep_month.get(k, 0)
    pct = calc_pct(oct_val, sep_val)
    print(f"{k}:")
    print(f"  Oct (1-8): ${oct_val:,.2f}")
    print(f"  Sep (Full Month): ${sep_val:,.2f}")
    print(f"  Percentage: {pct}\n")
    
oct_total = sum(oct_month.get(k, 0) for k in filter_hg(oct_month).keys() if k != 'EBAY-RUGSFOREVER')
sep_total = sum(sep_month.get(k, 0) for k in filter_hg(oct_month).keys() if k != 'EBAY-RUGSFOREVER')
print(f"TOTAL:")
print(f"  Oct (1-8): ${oct_total:,.2f}")
print(f"  Sep (Full Month): ${sep_total:,.2f}")
print(f"  Percentage: {calc_pct(oct_total, sep_total)}\n")

print("SALES COUNT:")
oct_count = oct_month.get("order_count_hg", 0)
sep_count = sep_month.get("order_count_hg", 0)
print(f"  Oct (1-8): {oct_count}")
print(f"  Sep (Full Month): {sep_count}")
print(f"  Percentage: {calc_pct(oct_count, sep_count)}")
