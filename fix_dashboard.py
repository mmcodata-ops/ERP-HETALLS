import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the Promise.all .then block
old_then = '''        ]).then(([k, r, o, tData, c]) => {
          if (!isMounted) return;
          if (isServerDown) {
            window.location.reload();
            return;
          }
          setKpis(k.data);
          setRevenueChart(r.data);
          setRecentOrders(o.data);
          setTodayOrders(tData.data);
          setCompaniesRev(c.data);
          setLastRefreshed(new Date());
        }).catch((err) => {'''

new_then = '''        ]).then(([k, r, o, tData, c]) => {
          if (!isMounted) return;
          if (isServerDown) {
            window.location.reload();
            return;
          }
          
          const checkUpdate = (prev, next) => JSON.stringify(prev) === JSON.stringify(next) ? prev : next;
          
          let didUpdate = false;
          setKpis(prev => { const next = checkUpdate(prev, k.data); if (prev !== next) didUpdate = true; return next; });
          setRevenueChart(prev => { const next = checkUpdate(prev, r.data); if (prev !== next) didUpdate = true; return next; });
          setRecentOrders(prev => { const next = checkUpdate(prev, o.data); if (prev !== next) didUpdate = true; return next; });
          setTodayOrders(prev => { const next = checkUpdate(prev, tData.data); if (prev !== next) didUpdate = true; return next; });
          setCompaniesRev(prev => { const next = checkUpdate(prev, c.data); if (prev !== next) didUpdate = true; return next; });
          
          if (didUpdate || isInitial) {
            setLastRefreshed(new Date());
          }
        }).catch((err) => {'''

code = code.replace(old_then, new_then)

# Re-add interval
old_interval = '''    fetchAll(true);
    return () => {
      isMounted = false;
    };
  }, [API]);'''

new_interval = '''    fetchAll(true);
    const interval = setInterval(() => fetchAll(false), 15000);
    return () => {
      isMounted = false;
      clearInterval(interval);
    };
  }, [API]);'''

code = code.replace(old_interval, new_interval)

with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated Dashboard.jsx")
