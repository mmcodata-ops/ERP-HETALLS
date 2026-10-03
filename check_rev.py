import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of RevenueSpinningCard
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
# Be careful here!
orders_code = orders_code.replace('$<span style={{ fontWeight: \\'bold\\', color: \\'var(--text)\\' }}></span>',
                                  '<span style={{ fontWeight: \\'bold\\', color: \\'var(--text)\\' }}>{c.order_count}</span>')
# Wait, the Revenue card renders it as:
# <span style={{ fontWeight: 'bold', color: 'var(--text)' }}></span>
# Let's check exactly how it's written in RevenueSpinningCard

