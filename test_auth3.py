import requests

login_data = {
    'username': 'shyoji.ram.(it)@hetalls.com',
    'password': '123'
}
res = requests.post('http://127.0.0.1:8000/api/auth/login', data=login_data)
if res.status_code != 200:
    print("LOGIN FAILED", res.status_code, res.text)
    exit(1)
token = res.json().get('access_token')

headers = {'Authorization': f'Bearer {token}'}
kpis = requests.get('http://127.0.0.1:8000/api/dashboard/kpis', headers=headers)
print("KPIS:", kpis.status_code)
if kpis.status_code != 200:
    print(kpis.text)
else:
    print(kpis.json())
