import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract RevenueSpinningCard
match = re.search(r'const RevenueSpinningCard = .*?\n};\n', content, re.DOTALL)
if match:
    rev_code = match.group(0)
    # Create OrdersSpinningCard from it
    orders_code = rev_code.replace('RevenueSpinningCard', 'OrdersSpinningCard')
    orders_code = orders_code.replace('kpis?.today_revenue', 'kpis?.today_orders')
    orders_code = orders_code.replace('kpis?.this_month_revenue', 'kpis?.this_month_orders')
    orders_code = orders_code.replace('kpis?.this_year_revenue', 'kpis?.this_year_orders')
    
    # We also need isOrdersUp for the color/icon of Today's Orders. Let's pass it as a prop or calculate it.
    # To keep it simple, pass isOrdersUp as a prop.
    orders_code = orders_code.replace('({ kpis, companiesRev, style = {} }) => {', '({ kpis, companiesRev, isOrdersUp, style = {} }) => {')
    
    orders_code = orders_code.replace('''{ key: 'today', label: "Today's Revenue", value: kpis?.today_revenue || 0, sub: "Today only", icon: DollarSign, colorClass: 'gold' }''',
                                      '''{ key: 'today', label: "Orders Today", value: kpis?.today_orders || 0, sub: "Today only", icon: isOrdersUp ? TrendingUp : TrendingDown, colorClass: isOrdersUp ? 'success' : 'danger' }''')
    orders_code = orders_code.replace('''{ key: 'month', label: "This Month Revenue", value: kpis?.this_month_revenue || 0, sub: "Month to date", icon: DollarSign, colorClass: 'gold' }''',
                                      '''{ key: 'month', label: "Orders This Month", value: kpis?.this_month_orders || 0, sub: "Month to date", icon: TrendingUp, colorClass: 'warning' }''')
    orders_code = orders_code.replace('''{ key: 'year', label: "This Year Revenue", value: kpis?.this_year_revenue || 0, sub: "Financial year", icon: DollarSign, colorClass: 'gold' }''',
                                      '''{ key: 'year', label: "Orders This Year", value: kpis?.this_year_orders || 0, sub: "Year to date", icon: TrendingUp, colorClass: 'success' }''')
                                      
    orders_code = orders_code.replace('Companies Revenue', 'Companies Orders')
    orders_code = orders_code.replace('c.value.toLocaleString()', 'c.order_count')
    orders_code = orders_code.replace('$', '')

    content = content.replace('const RevenueSpinningCard = ', orders_code + '\nconst RevenueSpinningCard = ')
    
    # Now replace the inline cube-container in kpiElements with OrdersSpinningCard
    
    kpi_elements_match = re.search(r'(<div \s*key="orders".*?</div>\s*</div>)', content, re.DOTALL)
    
    # Wait, the inline cube-container has a specific structure. Let's find the exact string.
