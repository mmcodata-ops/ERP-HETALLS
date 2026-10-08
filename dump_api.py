import sys
sys.path.insert(0, './backend')
import routers.dashboard
from unittest.mock import MagicMock

routers.dashboard.get_current_user = MagicMock(return_value={"id": 1})

res = routers.dashboard.revenue_chart(group_by="day", current_user={"id": 1})
for r in res:
    if r.get("month") == "Sep 2026":
        print("SEP 2026:")
        print(r)
