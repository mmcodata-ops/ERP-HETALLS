import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Did I accidentally inject a broken OrdersSpinningCard somewhere?
# No, we established that match was None, so it wasn't injected!
# Wait, if match was None, how did <OrdersSpinningCard...> get put into kpiElements?
# Ah! I used e.sub(pattern, new_block, content, flags=re.DOTALL) which didn't depend on match!

start_idx = content.find('const RevenueSpinningCard =')
end_idx = content.find('// ── Status Badge', start_idx)

rev_code = content[start_idx:end_idx]

orders_code = rev_code.replace('RevenueSpinningCard', 'OrdersSpinningCard')
orders_code = orders_code.replace('kpis?.today_revenue', 'kpis?.today_orders')
orders_code = orders_code.replace('kpis?.this_month_revenue', 'kpis?.this_month_orders')
orders_code = orders_code.replace('kpis?.this_year_revenue', 'kpis?.this_year_orders')

orders_code = orders_code.replace('({ kpis, companiesRev, style = {} }) => {', '({ kpis, companiesRev, isOrdersUp, style = {} }) => {')

orders_code = orders_code.replace('''{ key: 'today', label: "Today's Revenue", value: kpis?.today_revenue || 0, sub: "Today only", icon: DollarSign, colorClass: 'gold' }''',
                                  '''{ key: 'today', label: "Orders Today", value: kpis?.today_orders || 0, sub: "Today only", icon: isOrdersUp ? TrendingUp : TrendingDown, colorClass: isOrdersUp ? 'success' : 'danger' }''')
orders_code = orders_code.replace('''{ key: 'month', label: "This Month Revenue", value: kpis?.this_month_revenue || 0, sub: "Month to date", icon: DollarSign, colorClass: 'gold' }''',
                                  '''{ key: 'month', label: "Orders This Month", value: kpis?.this_month_orders || 0, sub: "Month to date", icon: TrendingUp, colorClass: 'warning' }''')
orders_code = orders_code.replace('''{ key: 'year', label: "This Year Revenue", value: kpis?.this_year_revenue || 0, sub: "Financial year", icon: DollarSign, colorClass: 'gold' }''',
                                  '''{ key: 'year', label: "Orders This Year", value: kpis?.this_year_orders || 0, sub: "Year to date", icon: TrendingUp, colorClass: 'success' }''')

orders_code = orders_code.replace('Companies Revenue', 'Companies Orders')

old_span = "<span style={{ fontWeight: 'bold', color: 'var(--text)' }}></span>"
new_span = "<span style={{ fontWeight: 'bold', color: 'var(--text)' }}>{c.order_count}</span>"
orders_code = orders_code.replace(old_span, new_span)

orders_code = orders_code.replace('isCurrency ? "currency" : "number"', '"number"')
orders_code = orders_code.replace('format="currency"', 'format="number"')

content = content.replace('const RevenueSpinningCard =', orders_code + '\nconst RevenueSpinningCard =')

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected OrdersSpinningCard properly")
