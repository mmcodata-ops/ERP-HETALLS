import requests
res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'})
token = res.json().get('access_token')
headers = {'Authorization': f'Bearer {token}'}

for ep in ['kpis', 'companies-revenue', 'revenue-chart', 'recent-orders', 'today-orders']:
    r = requests.get(f'https://hetalls-erp-b.onrender.com/api/dashboard/{ep}', headers=headers)
    print(f"{ep}: {r.status_code}")
    if r.status_code != 200:
        print(r.text)
