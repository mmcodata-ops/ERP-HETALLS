import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# The exact block to replace
old_block = '''    const kpiElements = [
    <RevenueSpinningCard key="rev" kpis={kpis} companiesRev={companiesRev ? { today: companiesRev.today?.filter(c => !c.name?.toUpperCase().includes('HETALLS')), month: companiesRev.month?.filter(c => !c.name?.toUpperCase().includes('HETALLS')), year: companiesRev.year?.filter(c => !c.name?.toUpperCase().includes('HETALLS')), total: companiesRev.total?.filter(c => !c.name?.toUpperCase().includes('HETALLS')) } : null} style={{ viewTransitionName: 'kpi-rev' }} />,
    <div 
      key="orders"
      className="cube-container" 
      onMouseDown={startSpin}
      onMouseUp={stopSpin}
      onMouseLeave={stopSpin}
      onTouchStart={startSpin}
      onTouchEnd={stopSpin}
      onDragStart={(e) => e.preventDefault()}
      style={{ cursor: 'pointer', userSelect: 'none', viewTransitionName: 'kpi-orders' }}
    >
      <div 
        className="cube" 
        ref={cubeRef}
        style={{ 
          transform: 	ranslateZ(-140px) rotateY(deg), 
          transition: 'transform 0.4s ease-out' 
        }}
      >
        <div className="cube-face"><div style={{ width: '100%', height: '100%' }}><KPICard icon={isOrdersUp ? TrendingUp : TrendingDown} label="Orders Today" value={kpis?.today_orders} sub="Today only" colorClass={isOrdersUp ? "success" : "danger"} /></div></div>
        <div className="cube-face"><div style={{ width: '100%', height: '100%' }}><KPICard icon={TrendingUp} label="Orders This Month" value={kpis?.this_month_orders} sub="Month to date" colorClass="warning" /></div></div>
        <div className="cube-face"><div style={{ width: '100%', height: '100%' }}><KPICard icon={TrendingUp} label="Orders This Year" value={kpis?.this_year_orders} sub="Year to date" colorClass="success" /></div></div>
      </div>
    </div>,'''

# Regex to safely replace the orders block
pattern = r'<div \s*key="orders".*?</div>\s*</div>\s*</div>,'

new_block = '''<OrdersSpinningCard key="orders" kpis={kpis} isOrdersUp={isOrdersUp} companiesRev={companiesRev ? { today: companiesRev.today?.filter(c => !c.name?.toUpperCase().includes('HETALLS')), month: companiesRev.month?.filter(c => !c.name?.toUpperCase().includes('HETALLS')), year: companiesRev.year?.filter(c => !c.name?.toUpperCase().includes('HETALLS')), total: companiesRev.total?.filter(c => !c.name?.toUpperCase().includes('HETALLS')) } : null} style={{ viewTransitionName: 'kpi-orders' }} />,'''

new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced orders block with OrdersSpinningCard")
