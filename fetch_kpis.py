import urllib.request
try:
    print(urllib.request.urlopen('http://127.0.0.1:8000/api/dashboard/kpis').read().decode())
except Exception as e:
    print(e)
