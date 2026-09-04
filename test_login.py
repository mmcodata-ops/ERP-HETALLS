import requests

login_data = {
    'username': 'admin@hetalls.com',
    'password': 'adminpassword'
}
res = requests.post('http://127.0.0.1:8000/api/auth/token', data=login_data)
print(res.status_code, res.text)
