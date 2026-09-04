import requests
import json
try:
    res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'})
    token = res.json().get('access_token')
    headers = {'Authorization': f'Bearer {token}'}

    r = requests.get('https://hetalls-erp-b.onrender.com/api/dashboard/today-orders', headers=headers)
    print(r.text)
except Exception as e:
    print('Exception:', e)
