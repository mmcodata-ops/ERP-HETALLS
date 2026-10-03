import base64

python_code = b'''
import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const RevenueSpinningCard =')
end = content.find('// ── Status Badge', start)
rev = content[start:end]

ord_c = rev.replace('RevenueSpinningCard', 'OrdersSpinningCard')
ord_c = ord_c.replace('kpis?.today_revenue', 'kpis?.today_orders')
ord_c = ord_c.replace('kpis?.this_month_revenue', 'kpis?.this_month_orders')
ord_c = ord_c.replace('kpis?.this_year_revenue', 'kpis?.this_year_orders')
ord_c = ord_c.replace('({ kpis, companiesRev, style = {} }) => {', '({ kpis, companiesRev, isOrdersUp, style = {} }) => {')

ord_c = ord_c.replace("{ key: 'today', label: \\\"Today's Revenue\\\", value: kpis?.today_revenue || 0, sub: \\\"Today only\\\", icon: DollarSign, colorClass: 'gold' }", "{ key: 'today', label: \\\"Orders Today\\\", value: kpis?.today_orders || 0, sub: \\\"Today only\\\", icon: isOrdersUp ? TrendingUp : TrendingDown, colorClass: isOrdersUp ? 'success' : 'danger' }")
ord_c = ord_c.replace("{ key: 'month', label: \\\"This Month Revenue\\\", value: kpis?.this_month_revenue || 0, sub: \\\"Month to date\\\", icon: DollarSign, colorClass: 'gold' }", "{ key: 'month', label: \\\"Orders This Month\\\", value: kpis?.this_month_orders || 0, sub: \\\"Month to date\\\", icon: TrendingUp, colorClass: 'warning' }")
ord_c = ord_c.replace("{ key: 'year', label: \\\"This Year Revenue\\\", value: kpis?.this_year_revenue || 0, sub: \\\"Financial year\\\", icon: DollarSign, colorClass: 'gold' }", "{ key: 'year', label: \\\"Orders This Year\\\", value: kpis?.this_year_orders || 0, sub: \\\"Year to date\\\", icon: TrendingUp, colorClass: 'success' }")

ord_c = ord_c.replace('Companies Revenue', 'Companies Orders')
ord_c = ord_c.replace('$<span style={{ fontWeight: \\'bold\\', color: \\'var(--text)\\' }}></span>', '<span style={{ fontWeight: \\'bold\\', color: \\'var(--text)\\' }}>{c.order_count}</span>')

# Fix format
ord_c = ord_c.replace('format=\"currency\"', 'format=\"number\"')
ord_c = ord_c.replace('format=\\\'currency\\\'', 'format=\\\'number\\\'')

content = content.replace('const RevenueSpinningCard =', ord_c + '\\nconst RevenueSpinningCard =')
with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
'''

with open('fix_dash_b64.py', 'wb') as f:
    f.write(python_code)

