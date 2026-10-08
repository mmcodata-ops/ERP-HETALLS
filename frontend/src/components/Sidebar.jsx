import React, { useEffect, useRef, useState } from 'react'
import { NavLink, useNavigate, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useMessages } from '../context/MessagesContext'
import {
  LayoutDashboard, ShoppingCart, Package, DollarSign,
  Users, BarChart2, Settings, LogOut, Layers, MessageSquare, X
} from 'lucide-react'

const NAV = [
  { label: 'Main', items: [
    { to: '/dashboard',  icon: LayoutDashboard, label: 'Dashboard',   permission: 'dashboard' },
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
  }, [location.pathname])

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
                {visible.map(item => (
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
              ))}
            </div>
          )
        })}
      </nav>

      <div style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderTop: '1px solid var(--border-color)' }}>
        <span style={{ fontSize: '13px', fontWeight: 500, color: 'var(--text-muted)' }}>Forecast View</span>
        <label style={{ cursor: 'pointer', display: 'flex', alignItems: 'center' }}>
          <input type="checkbox" style={{ display: 'none' }} checked={location.pathname === '/forecast'} onChange={(e) => navigate(e.target.checked ? '/forecast' : '/dashboard')} />
          <div style={{ width: '32px', height: '18px', background: location.pathname === '/forecast' ? 'var(--primary-color)' : 'rgba(255,255,255,0.1)', borderRadius: '9px', position: 'relative', transition: 'background 0.3s' }}>
            <div style={{ width: '14px', height: '14px', background: '#fff', borderRadius: '50%', position: 'absolute', top: '2px', left: location.pathname === '/forecast' ? '16px' : '2px', transition: 'left 0.3s' }} />
          </div>
        </label>
      </div>
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
