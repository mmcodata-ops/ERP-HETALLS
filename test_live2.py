import requests

login_data = {
    'username': 'shyoji.ram.(it)@hetalls.com',
    'password': '123'
}
try:
    res = requests.post('https://hetalls-erp-b.onrender.com/api/auth/login', data=login_data)
    token = res.json().get('access_token')

    headers = {'Authorization': f'Bearer {token}'}
    kpis = requests.get('https://hetalls-erp-b.onrender.com/api/dashboard/kpis', headers=headers)
    print("LIVE KPIS:", kpis.status_code)
    if kpis.status_code != 200:
        print(kpis.text)
    else:
        print(kpis.json())
except Exception as e:
    print(e)
