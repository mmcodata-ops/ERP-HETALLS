import os

file_path = 'frontend/src/components/Sidebar.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Forecast from NAV
target_nav = "    { to: '/forecast',   icon: BarChart2,       label: 'Sales Forecast', permission: 'dashboard' },\n"
content = content.replace(target_nav, "")

# Add cute checkbox above sidebar-user
target_user = '      <div className="sidebar-user">'
cute_checkbox = """      <div style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderTop: '1px solid var(--border-color)' }}>
        <span style={{ fontSize: '13px', fontWeight: 500, color: 'var(--text-muted)' }}>Forecast View</span>
        <label style={{ cursor: 'pointer', display: 'flex', alignItems: 'center' }}>
          <input type="checkbox" style={{ display: 'none' }} checked={location.pathname === '/forecast'} onChange={(e) => navigate(e.target.checked ? '/forecast' : '/dashboard')} />
          <div style={{ width: '32px', height: '18px', background: location.pathname === '/forecast' ? 'var(--primary-color)' : 'rgba(255,255,255,0.1)', borderRadius: '9px', position: 'relative', transition: 'background 0.3s' }}>
            <div style={{ width: '14px', height: '14px', background: '#fff', borderRadius: '50%', position: 'absolute', top: '2px', left: location.pathname === '/forecast' ? '16px' : '2px', transition: 'left 0.3s' }} />
          </div>
        </label>
      </div>
      <div className="sidebar-user">"""
content = content.replace(target_user, cute_checkbox)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar updated")
