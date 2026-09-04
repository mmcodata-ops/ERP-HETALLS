import requests
res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data={'username': 'shyoji.ram.(it)@hetalls.com', 'password': '123'})
print(res.status_code)
print(res.text)
