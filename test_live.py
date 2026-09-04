import urllib.request
try:
    req = urllib.request.Request('https://hetalls-erp-b.onrender.com/api/dashboard/kpis')
    print(urllib.request.urlopen(req).read().decode())
except Exception as e:
    print(e)
