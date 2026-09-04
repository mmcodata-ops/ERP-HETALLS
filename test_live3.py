import requests
login_data = {'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'}
try:
    res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data=login_data)
    token = res.json().get('access_token')
    headers = {'Authorization': f'Bearer {token}'}

    for ep in ['kpis', 'companies-revenue', 'revenue-chart', 'recent-orders', 'today-orders']:
        r = requests.get(f'https://hetalls-erp-b.onrender.com/api/dashboard/{ep}', headers=headers)
        print(f"{ep}: {r.status_code}")
        if r.status_code != 200:
            print(r.text)
except Exception as e:
    print(e)
