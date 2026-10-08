import React, { useEffect, useRef, useState } from 'react'
import { NavLink, useNavigate, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useMessages } from '../context/MessagesContext'
import {
  LayoutDashboard, ShoppingCart, Package, DollarSign,
  Users, BarChart2, Settings, LogOut, Layers, MessageSquare, X, ChevronDown, ChevronRight, Monitor
} from 'lucide-react'

const NAV = [
  { label: 'Main', items: [
    { 
      label: 'Dashboards', 
      icon: LayoutDashboard, 
      permission: 'dashboard',
      dropdown: [
        { to: '/dashboard', label: 'Main Dashboard' },
        { to: '/forecast',  label: 'Site Preview' }
      ]
    },
  ]},
  { label: 'Finance & People', items: [
    { to: '/accounts',   icon: DollarSign,      label: 'Accounts',    permission: 'accounts' },
  ]},
  { label: 'Intelligence', items: [
    { to: '/reports',    icon: BarChart2,       label: 'Reports',     permission: 'reports' },
  ]},
  { label: 'System', items: [
    { to: '/settings',   icon: Settings,        label: 'Settings',    role: 'admin' },
  ]},
]

export default function Sidebar({ sidebarOpen, setSidebarOpen }) {
  const { user, logout } = useAuth()
  const { unreadCount } = useMessages()
  const navigate = useNavigate()
  const location = useLocation()
  const navRef = useRef(null)
  const [pillStyle, setPillStyle] = useState({ top: 0, height: 0, opacity: 0 })
  const [openDropdowns, setOpenDropdowns] = useState({ 'Dashboards': true })

  useEffect(() => {
    // Wait for render, then find active element
    setTimeout(() => {
      if (!navRef.current) return
      const activeEl = navRef.current.querySelector('.nav-item.active')
      if (activeEl) {
        setPillStyle({
          top: activeEl.offsetTop,
          height: activeEl.offsetHeight,
          opacity: 1
        })
      } else {
        setPillStyle(p => ({ ...p, opacity: 0 }))
      }
    }, 50)
  }, [location.pathname, openDropdowns])

  const canSee = (item) => {
    if (!item.role && !item.permission) return true
    const uRole = (user?.role || '').toLowerCase()
    const uPerms = (user?.permissions || []).map(p => p.toLowerCase())
    if (uRole === 'admin') return true
    if (item.role && uRole === item.role.toLowerCase()) return true
    if (item.permission && uPerms.includes(item.permission.toLowerCase())) return true
    return false
  }

  const initials = user?.name
    ? user.name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
    : 'U'

  return (
    <>
      {sidebarOpen && (
        <div 
          className="mobile-backdrop" 
          onClick={() => setSidebarOpen && setSidebarOpen(false)} 
        />
      )}
      <aside className={`sidebar ${sidebarOpen ? 'mobile-open' : ''}`}>
        <div className="sidebar-logo">
          <div className="logo-mark" style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <div className="logo-icon">H</div>
              <div className="logo-text">
                <h1>Hetalls ERP</h1>
                <span>Management System</span>
              </div>
            </div>
            <button 
              className="mobile-close-btn" 
              onClick={() => setSidebarOpen && setSidebarOpen(false)}
              title="Close Menu"
            >
              <X size={20} />
            </button>
          </div>
        </div>

        <nav className="sidebar-nav" ref={navRef} style={{ position: 'relative' }}>
          <div className="sidebar-pill" style={{
            position: 'absolute',
            top: pillStyle.top,
            height: pillStyle.height,
            left: 12,
            right: 12,
            opacity: pillStyle.opacity,
            borderRadius: '50px',
            background: 'rgba(255, 255, 255, 0.1)', backdropFilter: 'blur(20px)', WebkitBackdropFilter: 'blur(20px)',
            border: '1px solid rgba(255, 255, 255, 0.15)', borderTop: '1px solid rgba(255, 255, 255, 0.25)',
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.2)',
            transition: 'all 0.35s cubic-bezier(0.34, 1.4, 0.64, 1)',
            pointerEvents: 'none',
            zIndex: 0
          }} />
          {NAV.map(section => {
            const visible = section.items.filter(i => canSee(i))
            if (!visible.length) return null

            return (
              <div key={section.label}>
                <div className="nav-section-label">{section.label}</div>
                {visible.map(item => {
                  if (item.dropdown) {
                    return (
                      <div key={item.label}>
                        <div 
                          className="nav-item" 
                          style={{ cursor: 'pointer', position: 'relative', zIndex: 1 }}
                          onClick={() => setOpenDropdowns(p => ({ ...p, [item.label]: !p[item.label] }))}
                        >
                          <item.icon size={17} />
                          {item.label}
                          <span style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center' }}>
                            {openDropdowns[item.label] ? <ChevronDown size={14}/> : <ChevronRight size={14}/>}
                          </span>
                        </div>
                        <div style={{ 
                          height: openDropdowns[item.label] ? 'auto' : 0, 
                          overflow: 'hidden', 
                          display: 'flex', 
                          flexDirection: 'column',
                          paddingLeft: '12px'
                        }}>
                          {item.dropdown.map(sub => (
                            <NavLink
                              key={sub.to}
                              to={sub.to}
                              end
                              onClick={() => setSidebarOpen && setSidebarOpen(false)}
                              style={{ position: 'relative', zIndex: 1, padding: '8px 12px', minHeight: '36px', marginTop: '4px' }}
                              className={({ isActive }) => `nav-item${isActive ? ' active' : ''}`}
                            >
                              <div style={{ width: '4px', height: '4px', background: 'currentColor', borderRadius: '50%', marginRight: '12px', opacity: 0.5 }} />
                              {sub.label}
                            </NavLink>
                          ))}
                        </div>
                      </div>
                    )
                  }

                  return (
                    <NavLink
                      key={item.to}
                      to={item.to}
                      end
                      onClick={() => setSidebarOpen && setSidebarOpen(false)}
                      style={{ position: 'relative', zIndex: 1 }}
                      className={({ isActive }) => `nav-item${isActive ? ' active' : ''}`}
                    >
                    <item.icon size={17} />
                    {item.label}
                    {item.label === 'Messages' && unreadCount > 0 && (
                      <span style={{
                        marginLeft: 'auto',
                        backgroundColor: 'var(--danger)',
                        color: '#fff',
                        fontSize: '11px',
                        fontWeight: 'bold',
                        borderRadius: '10px',
                        padding: '2px 6px',
                        minWidth: '18px',
                        textAlign: 'center'
                      }}>
                        {unreadCount}
                      </span>
                    )}
                  </NavLink>
                  )
                })}
            </div>
          )
        })}
      </nav>

      <div className="sidebar-user">
        <div className="user-avatar">{initials}</div>
        <div className="user-info">
          <div className="name">{user?.name}</div>
          <div className="role">{user?.role}</div>
        </div>
        <button
          className="logout-btn"
          title="Logout"
          onClick={() => { logout(); navigate('/login') }}
        >
          <LogOut size={16} />
        </button>
      </div>
    </aside>
    </>
  )
}
