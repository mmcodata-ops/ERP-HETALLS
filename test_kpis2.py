import requests
import time
res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'})
token = res.json().get('access_token')
headers = {'Authorization': f'Bearer {token}'}

t0 = time.time()
kpis = requests.get('https://hetalls-erp-b.onrender.com/api/dashboard/kpis', headers=headers)
print(kpis.status_code)
print(f"Time taken: {time.time() - t0} seconds")
