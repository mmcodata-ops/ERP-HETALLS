import httpx
import time

try:
    # Try calling the local server if it's running
    res = httpx.get("http://localhost:8000/api/dashboard/revenue-chart?group_by=mtd", headers={"Authorization": "Bearer TEST"})
    print(res.status_code)
    data = res.json()
    sep = [d for d in data if d.get('month') == 'Sep 2026']
    print(sep)
except Exception as e:
    print("Server not running:", e)
