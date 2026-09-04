import requests
res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'})
token = res.json().get('access_token')
headers = {'Authorization': f'Bearer {token}'}

print("KPIS:")
kpis = requests.get('https://hetalls-erp-b.onrender.com/api/dashboard/kpis', headers=headers)
print(kpis.status_code)
if kpis.status_code != 200: print(kpis.text)
else: print(kpis.json())
