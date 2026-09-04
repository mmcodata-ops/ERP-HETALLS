import requests

login_data = {
    'username': 'shyoji.ram.(it)@hetalls.com',
    'password': '123'
}
res = requests.post('http://127.0.0.1:8000/api/auth/token', data=login_data)
token = res.json().get('access_token')

headers = {'Authorization': f'Bearer {token}'}
kpis = requests.get('http://127.0.0.1:8000/api/dashboard/kpis', headers=headers)
print("KPIS:", kpis.status_code)
if kpis.status_code != 200:
    print(kpis.text)
    
charts = requests.get('http://127.0.0.1:8000/api/dashboard/revenue-chart', headers=headers)
print("CHARTS:", charts.status_code)
if charts.status_code != 200:
    print(charts.text)
