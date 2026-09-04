import requests
import json
try:
    res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'}, timeout=30)
    token = res.json().get('access_token')
    headers = {'Authorization': f'Bearer {token}'}

    for ep in ['kpis', 'revenue-chart', 'recent-orders', 'today-orders', 'companies-revenue']:
        r = requests.get(f'https://hetalls-erp-b.onrender.com/api/dashboard/{ep}', headers=headers, timeout=30)
        print(f"{ep}: {r.status_code}")
except Exception as e:
    print('Exception:', e)
