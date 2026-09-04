import requests
import json
res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'})
token = res.json().get('access_token')
headers = {'Authorization': f'Bearer {token}'}

r = requests.get('https://hetalls-erp-b.onrender.com/api/dashboard/kpis', headers=headers)
print(json.dumps(r.json(), indent=2))
