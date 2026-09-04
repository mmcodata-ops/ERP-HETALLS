with open('dashboard.py', 'r', encoding='utf-8') as f:
    print('orders.sort(key=lambda x: x["date"], reverse=True)' in f.read())
