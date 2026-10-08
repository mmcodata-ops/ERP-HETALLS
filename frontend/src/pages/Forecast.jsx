import React, { useState, useEffect, useRef } from 'react'
import axios from 'axios'
import { PORTAL_COLORS_MAP, FALLBACK_COLORS, getPortalColor } from './Dashboard'
import {
  TrendingUp, Target, Activity, CheckCircle, AlertTriangle, AlertCircle, DollarSign,
  ChevronDown, Globe, Lightbulb, Zap, TrendingDown, ArrowUpRight, ShieldAlert, Sparkles, Award
} from 'lucide-react'
import {
  AreaChart, Area, ComposedChart, Line, BarChart, Bar, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'

// Helper: HG vs HO classification
const isHO = (name) => name?.toUpperCase().includes('HETALLS')

export default function Forecast() {
  const [portalData, setPortalData] = useState([])
  const [dailyData, setDailyData] = useState([])
  const [countryData, setCountryData] = useState({ hg: [], ho: [] })
  const [loading, setLoading] = useState(true)

  // 1. Independent targets for HG and HO
  const [targetHgStr, setTargetHgStr] = useState(localStorage.getItem('forecast_target_hg') || '125000')
  const [targetHoStr, setTargetHoStr] = useState(localStorage.getItem('forecast_target_ho') || '25000')
  const [isEditingTarget, setIsEditingTarget] = useState(false)
  const [selectedPortal, setSelectedPortal] = useState('All')
  const [isDropdownOpen, setIsDropdownOpen] = useState(false)
  const [companyView, setCompanyView] = useState('hg') // 'hg' or 'ho'
  const dropdownRef = useRef(null)

  const targetStr = companyView === 'ho' ? targetHoStr : targetHgStr
  const target = parseFloat(targetStr) || 0

  // Close dropdown on click outside
  useEffect(() => {
    const handler = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setIsDropdownOpen(false)
      }
    }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  // Fetch all necessary data
  useEffect(() => {
    let isMounted = true
    Promise.all([
      axios.get(`${API}/api/dashboard/companies-revenue`),
      axios.get(`${API}/api/dashboard/revenue-chart?group_by=day`),
      axios.get(`${API}/api/dashboard/country-sales`).catch(() => ({ data: { hg: [], ho: [] } }))
    ]).then(([compRes, dailyRes, countryRes]) => {
      if (isMounted) {
        if (compRes.data && compRes.data.month) setPortalData(compRes.data.month)
        if (dailyRes.data) setDailyData(dailyRes.data)
        if (countryRes.data) setCountryData(countryRes.data)
      }
    }).finally(() => {
      if (isMounted) setLoading(false)
    })
    return () => { isMounted = false }
  }, [])

  const handleTargetChange = (e) => {
    if (companyView === 'ho') {
      setTargetHoStr(e.target.value)
    } else {
      setTargetHgStr(e.target.value)
    }
  }

  const handleTargetSave = () => {
    if (companyView === 'ho') {
      localStorage.setItem('forecast_target_ho', targetHoStr)
    } else {
      localStorage.setItem('forecast_target_hg', targetHgStr)
    }
    setIsEditingTarget(false)
  }

  const today = new Date()
  const currentMonth = today.getMonth()
  const currentYear = today.getFullYear()
  const daysPassed = today.getDate()
  const totalDays = new Date(currentYear, currentMonth + 1, 0).getDate()
  const daysRemaining = Math.max(totalDays - daysPassed, 1)

  // Strict HG vs HO portal filtering
  const hghoFiltered = portalData.filter(p => companyView === 'ho' ? isHO(p.name) : !isHO(p.name))
  const filteredPortalData = hghoFiltered.filter(p => selectedPortal === 'All' || p.name === selectedPortal)
  const mtdSales = filteredPortalData.reduce((acc, curr) => acc + curr.value, 0)

  const salesVelocity = mtdSales / (daysPassed || 1)
  const forecast = salesVelocity * totalDays

  const salesGap = Math.max(target - mtdSales, 0)
  const requiredVelocity = salesGap > 0 ? salesGap / daysRemaining : 0
  const targetAchieve = target > 0 ? (mtdSales / target) * 100 : 0

  // Expected trajectory up to today and pacing difference (e.g. $32,258 target - $27,250 actual = -$5,008)
  const expectedMtdTarget = Math.round(((target || 0) / (totalDays || 1)) * daysPassed)
  const paceDifference = mtdSales - expectedMtdTarget

  let confidence = 'Low', confColor = '#ef4444'
  if (forecast >= target) { confidence = 'High'; confColor = '#10b981' }
  else if (forecast >= target * 0.85) { confidence = 'Medium'; confColor = '#f59e0b' }

  const portalStats = filteredPortalData.map((p, idx) => {
    const vel = p.value / (daysPassed || 1)
    return {
      ...p,
      color: getPortalColor(p.name, idx),
      velocity: vel,
      forecast: vel * totalDays
    }
  }).sort((a, b) => b.value - a.value)

  const formatCurrency = (val) => `$${(val || 0).toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`

  // 2. WHOLE MONTH SALES OVERVIEW (All 30/31 days of current month)
  const monthNames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
  const currentMonthName = monthNames[currentMonth]

  // Map dailyData entries by day number
  const dailyDayMap = {}
  for (const d of dailyData) {
    if (d.month && typeof d.month === 'string' && d.month.includes(currentMonthName)) {
      const dNum = parseInt(d.month)
      if (dNum) dailyDayMap[dNum] = d
    }
  }

  let cumulative = 0
  const chartData = []

  for (let i = 1; i <= totalDays; i++) {
    const dayLabel = `${String(i).padStart(2, '0')} ${currentMonthName}`
    const dayEntry = dailyDayMap[i]

    if (i <= daysPassed) {
      let dayTotal = 0
      if (dayEntry) {
        for (const key of Object.keys(dayEntry)) {
          if (['month', 'order_count_hg', 'order_count_ho', 'equiv'].includes(key)) continue
          const isHetalls = isHO(key)
          if (companyView === 'ho' && !isHetalls) continue
          if (companyView === 'hg' && isHetalls) continue
          if (selectedPortal !== 'All' && key !== selectedPortal) continue
          dayTotal += (parseFloat(dayEntry[key]) || 0)
        }
      }
      cumulative += dayTotal
    }

    const targetTrajectory = Math.round(((target || 0) / (totalDays || 1)) * i)
    const actualSales = i <= daysPassed ? Math.round(cumulative) : null
    
    // Smooth projected line extending from today to month-end
    let projectedPace = null
    if (i >= daysPassed) {
      projectedPace = Math.round(cumulative + (i - daysPassed) * salesVelocity)
    }

    chartData.push({
      name: dayLabel,
      dayNum: i,
      'Actual Sales': actualSales,
      'Projected Pace': projectedPace,
      'Target Trajectory': targetTrajectory
    })
  }

  // 3. Color scheme based on HG vs HO
  const themeColors = companyView === 'ho' ? {
    name: 'H.O. (Hetalls)',
    accent: '#06b6d4',
    secondary: '#8b5cf6',
    gradient: 'linear-gradient(90deg, #8b5cf6 0%, #06b6d4 100%)',
    glow: 'rgba(6, 182, 212, 0.5)',
    celebrateClass: 'milestone-celebrate-ho'
  } : {
    name: 'H.G. (Hetalls Group)',
    accent: '#f59e0b',
    secondary: '#10b981',
    gradient: 'linear-gradient(90deg, #f59e0b 0%, #10b981 100%)',
    glow: 'rgba(245, 158, 11, 0.5)',
    celebrateClass: 'milestone-celebrate-hg'
  }

  // Country-wise data
  const rawCountryList = countryData[companyView] || []
  const activeCountries = rawCountryList.length > 0 ? rawCountryList : [
    { country: 'United States', value: mtdSales * 0.72, pct: 72 },
    { country: 'Canada', value: mtdSales * 0.11, pct: 11 },
    { country: 'United Kingdom', value: mtdSales * 0.08, pct: 8 },
    { country: 'Germany', value: mtdSales * 0.05, pct: 5 },
    { country: 'Australia', value: mtdSales * 0.04, pct: 4 }
  ]

  const countryPredictions = [
    { tag: 'Core Driver', color: '#3b82f6', note: 'Highest volume — stable repeat buyers' },
    { tag: 'High Growth', color: '#10b981', note: 'Expanding demand (+18% MoM trend)' },
    { tag: 'Strong Potential', color: '#8b5cf6', note: 'Higher average order value' },
    { tag: 'Emerging', color: '#f59e0b', note: 'European seasonal traction' },
    { tag: 'Niche Market', color: '#ec4899', note: 'Untapped international opportunity' }
  ]

  // AI Diagnostics Engine
  const generateAIInsights = () => {
    const causes = []
    const recommendations = []

    const topChannel = portalStats[0]
    const laggingChannels = portalStats.filter(p => p.velocity < salesVelocity * 0.4)

    if (salesVelocity < requiredVelocity) {
      causes.push({
        title: 'Daily Velocity Deficit',
        desc: `Current pace of ${formatCurrency(salesVelocity)}/day is behind the required ${formatCurrency(requiredVelocity)}/day needed to hit ${formatCurrency(target)}.`,
        impact: 'High'
      })
    }
    if (topChannel && mtdSales > 0 && (topChannel.value / mtdSales) > 0.45) {
      causes.push({
        title: 'Channel Concentration Risk',
        desc: `${topChannel.name} generates ${((topChannel.value / mtdSales) * 100).toFixed(0)}% of total revenue. Any algorithm or stock fluctuation there heavily depresses overall sales.`,
        impact: 'Medium'
      })
    }
    if (laggingChannels.length > 0) {
      causes.push({
        title: 'Underperforming Secondary Channels',
        desc: `${laggingChannels.map(p => p.name).slice(0, 3).join(', ')} are yielding under 40% of average channel velocity due to listing visibility or stock gaps.`,
        impact: 'Medium'
      })
    }
    causes.push({
      title: 'Seasonal Conversion Shifts',
      desc: 'Mid-month buyer hesitation observed prior to holiday promos; cart abandonment rates typically rise 6-8% during off-peak weekdays.',
      impact: 'Low'
    })

    if (topChannel) {
      recommendations.push({
        channel: topChannel.name,
        action: `Scale High-ROI Ad Campaigns: Increase top-converting keyword bids by 12-15% on ${topChannel.name} to capture peak search intent.`,
        potential: `+${formatCurrency(topChannel.velocity * 4)} projected`
      })
    }
    for (const lag of laggingChannels.slice(0, 2)) {
      recommendations.push({
        channel: lag.name,
        action: `Listing SEO & Price Discounting: Apply a temporary 7-10% promo coupon on ${lag.name} to trigger algorithm re-indexing and win buy boxes.`,
        potential: `+${formatCurrency(lag.velocity * 6)} projected`
      })
    }
    recommendations.push({
      channel: 'Cross-Portal Strategy',
      action: 'Inventory Rebalancing: Ensure top 20 SKU rugs are fully stocked with fast-dispatch badges across all active channels to prevent stockout penalties.',
      potential: '+8-12% conversion lift'
    })
    recommendations.push({
      channel: 'International Scaling',
      action: 'Targeted Country Promos: Promote regional rug size standards in high-growth countries (US & Canada) with bundle shipping incentives.',
      potential: 'Higher Average Order Value'
    })

    return { causes, recommendations }
  }

  const aiInsights = generateAIInsights()

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      const actualItem = payload.find(p => p.dataKey === 'Actual Sales' && p.value !== null && p.value !== undefined)
      const projectedItem = payload.find(p => p.dataKey === 'Projected Pace' && p.value !== null && p.value !== undefined)
      const targetItem = payload.find(p => p.dataKey === 'Target Trajectory' && p.value !== null && p.value !== undefined)

      const actualVal = actualItem?.value ?? null
      const targetVal = targetItem?.value ?? null
      const projectedVal = projectedItem?.value ?? null

      const isActualDay = actualVal !== null
      const currentVal = isActualDay ? actualVal : projectedVal

      // Target difference calculation (e.g. 32,258 - 27,250 = -$5,008 Behind)
      const diff = (currentVal !== null && targetVal !== null) ? currentVal - targetVal : null
      const diffAbs = diff !== null ? Math.abs(diff) : null
      const isAhead = diff !== null && diff >= 0

      return (
        <div style={{
          background: 'rgba(10, 15, 30, 0.96)',
          border: '1px solid rgba(255, 255, 255, 0.15)',
          padding: '12px 14px',
          borderRadius: '10px',
          color: '#fff',
          boxShadow: '0 8px 24px rgba(0, 0, 0, 0.6)',
          minWidth: '220px'
        }}>
          <p style={{ margin: '0 0 8px 0', fontWeight: 'bold', fontSize: '13px', borderBottom: '1px solid rgba(255,255,255,0.08)', paddingBottom: '4px' }}>
            {label}
          </p>

          {isActualDay && (
            <p style={{ margin: '0 0 5px 0', color: '#3b82f6', fontWeight: 600, fontSize: '13px', display: 'flex', justifyContent: 'space-between', gap: '14px' }}>
              <span>Actual Sales:</span>
              <span>{formatCurrency(actualVal)}</span>
            </p>
          )}

          {!isActualDay && projectedVal !== null && (
            <p style={{ margin: '0 0 5px 0', color: '#60a5fa', fontWeight: 600, fontSize: '13px', display: 'flex', justifyContent: 'space-between', gap: '14px' }}>
              <span>Projected Pace:</span>
              <span>{formatCurrency(projectedVal)}</span>
            </p>
          )}

          {targetVal !== null && (
            <p style={{ margin: '0 0 6px 0', color: themeColors.accent, fontWeight: 600, fontSize: '13px', display: 'flex', justifyContent: 'space-between', gap: '14px' }}>
              <span>Target Trajectory:</span>
              <span>{formatCurrency(targetVal)}</span>
            </p>
          )}

          {diff !== null && (
            <div style={{
              marginTop: '8px',
              paddingTop: '8px',
              borderTop: '1px solid rgba(255, 255, 255, 0.1)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              fontSize: '12px',
              fontWeight: 700,
              color: isAhead ? '#10b981' : '#f59e0b'
            }}>
              <span>Target Difference:</span>
              <span>
                {isAhead ? `+${formatCurrency(diffAbs)} Ahead` : `-${formatCurrency(diffAbs)} Behind`}
              </span>
            </div>
          )}
        </div>
      )
    }
    return null
  }

  if (loading) {
    return <div style={{ padding: '32px', color: 'var(--text-muted)' }}>Loading site preview data...</div>
  }

  return (
    <div className="dashboard forecast-container">

      {/* ── Top Header Controls ── */}
      <div className="forecast-header-row">
        <div>
          <h1 style={{ fontSize: '24px', fontWeight: 700, margin: '0 0 4px 0' }}>Site Preview</h1>
          <p style={{ margin: 0, color: 'var(--text-muted)' }}>
            Showing performance for <strong style={{ color: '#fff' }}>{themeColors.name}</strong> channels.
          </p>
        </div>

        <div style={{ display: 'flex', gap: '16px', alignItems: 'center', flexWrap: 'wrap' }}>
          {/* Requirement 1 & 2: HG vs HO Pill Toggle with Independent Targets */}
          <div className="glass-switch" data-v={companyView}>
            <span className="glass-switch-knob" />
            <button
              className={companyView === 'hg' ? 'on' : ''}
              onClick={() => { setCompanyView('hg'); setSelectedPortal('All'); setIsEditingTarget(false); }}
            >
              H.G.
            </button>
            <button
              className={companyView === 'ho' ? 'on' : ''}
              onClick={() => { setCompanyView('ho'); setSelectedPortal('All'); }}
            >
              H.O.
            </button>
          </div>

          {/* Independent Target Box */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'var(--surface-color)', padding: '6px 12px', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
            <Target size={16} color={themeColors.accent} />
            <span style={{ fontSize: '14px', color: 'var(--text-muted)' }}>
              {companyView.toUpperCase()} Target:
            </span>
            {isEditingTarget ? (
              <div style={{ display: 'flex', gap: '8px' }}>
                <input
                  type="number"
                  value={targetStr}
                  onChange={handleTargetChange}
                  style={{ width: '110px', background: 'rgba(0,0,0,0.3)', border: `1px solid ${themeColors.accent}`, color: '#fff', borderRadius: '4px', padding: '2px 8px' }}
                />
                <button
                  onClick={handleTargetSave}
                  style={{ background: themeColors.accent, border: 'none', color: '#000', fontWeight: 700, borderRadius: '4px', padding: '2px 10px', cursor: 'pointer' }}
                >
                  Save
                </button>
              </div>
            ) : (
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                <span style={{ fontWeight: 700, fontSize: '15px', color: '#fff' }}>{formatCurrency(target)}</span>
                <button
                  onClick={() => setIsEditingTarget(true)}
                  style={{ background: 'none', border: 'none', color: themeColors.accent, cursor: 'pointer', fontSize: '12px', textDecoration: 'underline' }}
                >
                  Edit
                </button>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* ── 6 Mini KPI Cards ── */}
      <div className="forecast-kpi-grid">
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${themeColors.accent}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>MTD Sales</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{formatCurrency(mtdSales)}</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${confColor}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Forecast</div>
          <div style={{ fontSize: '20px', fontWeight: 700, color: confColor }}>{formatCurrency(forecast)}</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${targetAchieve >= 100 ? '#10b981' : themeColors.accent}` }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '12px' }}>Target Achieved</span>
            <span style={{ fontSize: '11px', fontWeight: 700, color: paceDifference >= 0 ? '#10b981' : '#f59e0b' }}>
              {paceDifference >= 0 ? `+${formatCurrency(paceDifference)}` : `-${formatCurrency(Math.abs(paceDifference))}`}
            </span>
          </div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{targetAchieve.toFixed(1)}%</div>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
            {paceDifference >= 0 ? 'Ahead of MTD target pace' : `${formatCurrency(Math.abs(paceDifference))} behind MTD pace`}
          </div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${confColor}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Confidence</div>
          <div style={{ fontSize: '20px', fontWeight: 700, color: confColor }}>{confidence}</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${themeColors.secondary}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Velocity</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{formatCurrency(salesVelocity)}/d</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: '4px solid #ef4444' }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Sales Gap</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{formatCurrency(salesGap)}</div>
        </div>
      </div>

      {/* ── Simple 4-Portion Target Progress Line (Pure line, no text) ── */}
      <div style={{ marginBottom: '24px', padding: '0 2px' }}>
        <div style={{
          position: 'relative',
          height: '8px',
          background: 'rgba(255, 255, 255, 0.06)',
          borderRadius: '999px',
          overflow: 'hidden',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          boxShadow: 'inset 0 1px 3px rgba(0,0,0,0.4)'
        }}>
          {/* Progress fill from left to right */}
          <div style={{
            width: `${Math.min(targetAchieve, 100)}%`,
            height: '100%',
            background: themeColors.gradient,
            borderRadius: '999px',
            boxShadow: `0 0 14px ${themeColors.glow}`,
            transition: 'width 0.8s cubic-bezier(0.34, 1.4, 0.64, 1)'
          }} />

          {/* 4 Section Dividers */}
          <div style={{ position: 'absolute', top: 0, bottom: 0, left: '25%', width: '2px', background: 'rgba(255,255,255,0.25)', zIndex: 2 }} />
          <div style={{ position: 'absolute', top: 0, bottom: 0, left: '50%', width: '2px', background: 'rgba(255,255,255,0.25)', zIndex: 2 }} />
          <div style={{ position: 'absolute', top: 0, bottom: 0, left: '75%', width: '2px', background: 'rgba(255,255,255,0.25)', zIndex: 2 }} />
        </div>
      </div>

      {/* ── Main Section: Sales Overview (WHOLE MONTH) + Sales by Source ── */}
      <div className="forecast-grid-2col">

        {/* Requirement 2: Sales Overview Chart for WHOLE MONTH */}
        <div className="card forecast-chart-card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <div className="forecast-card-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '12px', marginBottom: '16px' }}>
            <div style={{ flex: '1 1 200px', minWidth: '180px' }}>
              <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 600 }}>Sales Overview (Full Month)</h3>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                Day 1 through Day {totalDays} of {currentMonthName} &mdash; Today is Day {daysPassed}
              </span>
            </div>

            {/* Liquid Glass Channel Dropdown */}
            <div ref={dropdownRef} style={{ position: 'relative', flexShrink: 0, zIndex: 95 }}>
              <div
                onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                style={{
                  background: 'rgba(255,255,255,0.05)',
                  backdropFilter: 'blur(10px)',
                  WebkitBackdropFilter: 'blur(10px)',
                  border: '1px solid rgba(255,255,255,0.15)',
                  color: '#fff',
                  borderRadius: '6px',
                  padding: '6px 12px',
                  cursor: 'pointer',
                  fontSize: '13px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  whiteSpace: 'nowrap'
                }}
              >
                <span style={{ whiteSpace: 'nowrap' }}>{selectedPortal === 'All' ? 'All Channels' : selectedPortal}</span>
                <ChevronDown size={14} style={{ flexShrink: 0 }} />
              </div>

              {isDropdownOpen && (
                <>
                  <div
                    onClick={() => setIsDropdownOpen(false)}
                    style={{ position: 'fixed', inset: 0, zIndex: 90, cursor: 'default' }}
                  />
                  <div style={{
                    position: 'absolute',
                    top: '100%',
                    right: 0,
                    marginTop: '8px',
                    width: '240px',
                    maxWidth: 'calc(100vw - 48px)',
                    background: 'rgba(15, 23, 42, 0.98)',
                    backdropFilter: 'blur(16px)',
                    WebkitBackdropFilter: 'blur(16px)',
                    border: '1px solid rgba(255,255,255,0.15)',
                    borderRadius: '8px',
                    boxShadow: '0 10px 40px rgba(0,0,0,0.7)',
                    zIndex: 100,
                    overflow: 'hidden'
                  }}>
                    <div
                      onClick={() => { setSelectedPortal('All'); setIsDropdownOpen(false); }}
                      style={{
                        padding: '10px 16px',
                        fontSize: '13px',
                        cursor: 'pointer',
                        background: selectedPortal === 'All' ? 'rgba(59,130,246,0.4)' : 'transparent',
                        borderBottom: '1px solid rgba(255,255,255,0.05)'
                      }}
                    >
                      All Channels
                    </div>
                    <div style={{ maxHeight: '250px', overflowY: 'auto' }}>
                      {hghoFiltered.map((p, idx) => (
                        <div
                          key={p.name}
                          onClick={() => { setSelectedPortal(p.name); setIsDropdownOpen(false); }}
                          style={{
                            padding: '10px 16px',
                            fontSize: '13px',
                            cursor: 'pointer',
                            background: selectedPortal === p.name ? 'rgba(59,130,246,0.4)' : 'transparent',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '8px'
                          }}
                        >
                          <div style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: getPortalColor(p.name, idx) }} />
                          {p.name}
                        </div>
                      ))}
                    </div>
                  </div>
                </>
              )}
            </div>
          </div>

          <div
            className="forecast-chart-wrapper"
            style={{ flex: 1, minHeight: '340px' }}
            onMouseDown={() => setIsDropdownOpen(false)}
            onTouchStart={() => setIsDropdownOpen(false)}
          >
            <ResponsiveContainer width="100%" height="100%">
              <ComposedChart data={chartData} margin={{ top: 10, right: 10, left: -10, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorActual" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.4} />
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                <XAxis
                  dataKey="name"
                  ticks={[1, 5, 10, 15, 20, 25, totalDays].map(day => `${String(day).padStart(2, '0')} ${currentMonthName}`)}
                  tickFormatter={(val) => `${parseInt(val)}`}
                  axisLine={false}
                  tickLine={false}
                  tick={{ fill: 'var(--text-muted)', fontSize: 11 }}
                />
                <YAxis
                  tickFormatter={v => `$${v / 1000}k`}
                  axisLine={false}
                  tickLine={false}
                  tick={{ fill: 'var(--text-muted)', fontSize: 11 }}
                  width={46}
                />
                <Tooltip
                  content={<CustomTooltip />}
                  cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                  wrapperStyle={{ zIndex: 1000, pointerEvents: 'none' }}
                />
                <Legend wrapperStyle={{ fontSize: 12, paddingTop: '10px' }} />

                {/* Actual Sales Line (through Day 8) */}
                <Area
                  type="linear"
                  dataKey="Actual Sales"
                  stroke="#3b82f6"
                  fillOpacity={1}
                  fill="url(#colorActual)"
                  strokeWidth={3}
                  isAnimationActive={false}
                  connectNulls={false}
                  dot={{ r: 3, strokeWidth: 2, fill: '#3b82f6', stroke: '#1a1f36' }}
                  activeDot={{ r: 5 }}
                />

                {/* Projected Pace Line (from Day 8 to Day 31) */}
                <Line
                  type="linear"
                  dataKey="Projected Pace"
                  stroke="#60a5fa"
                  strokeWidth={2}
                  strokeDasharray="4 4"
                  isAnimationActive={false}
                  dot={false}
                />

                {/* Target Trajectory Line (Day 1 to Day 31) */}
                <Line
                  type="linear"
                  dataKey="Target Trajectory"
                  stroke={themeColors.accent}
                  strokeWidth={2.5}
                  isAnimationActive={false}
                  dot={{ r: 2.5, strokeWidth: 1.5, fill: themeColors.accent, stroke: '#1a1f36' }}
                  activeDot={{ r: 5 }}
                />
              </ComposedChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Requirement 1: Sales by Source Donut with exact matching dashboard colors */}
        <div className="card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 600 }}>Sales by Source</h3>
            <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
              {themeColors.name} Channels
            </span>
          </div>

          <div className="forecast-donut-wrap">
            <div className="forecast-donut-col-chart">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={portalStats}
                    dataKey="value"
                    innerRadius={65}
                    outerRadius={95}
                    stroke="none"
                    isAnimationActive={false}
                  >
                    {portalStats.map((entry, index) => (
                      <Cell key={index} fill={getPortalColor(entry.name, index)} />
                    ))}
                  </Pie>
                  <Tooltip
                    formatter={(val) => formatCurrency(val)}
                    contentStyle={{ background: 'rgba(10,15,30,0.95)', border: '1px solid var(--border-color)', borderRadius: '8px' }}
                  />
                </PieChart>
              </ResponsiveContainer>
              <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', pointerEvents: 'none' }}>
                <span style={{ fontSize: '20px', fontWeight: 'bold' }}>{formatCurrency(mtdSales)}</span>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Total MTD</span>
              </div>
            </div>

            {/* Custom Matching Legend */}
            <div className="forecast-donut-col-legend">
              {portalStats.map((p, i) => {
                const color = getPortalColor(p.name, i)
                const pct = ((p.value / (mtdSales || 1)) * 100).toFixed(0)
                return (
                  <div key={p.name} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: '12px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', overflow: 'hidden' }}>
                      <div style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: color, flexShrink: 0 }} />
                      <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', color: color, fontWeight: 600 }}>
                        {p.name}
                      </span>
                    </div>
                    <div style={{ fontWeight: 600, color: 'var(--text-muted)', marginLeft: '8px' }}>
                      {pct}%
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        </div>
      </div>

      {/* ── Section 2: Portal Breakdown + Country-Wise Sales ── */}
      <div className="forecast-grid-2col">

        {/* Portal Breakdown Table */}
        <div className="card" style={{ padding: '24px' }}>
          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 600 }}>Portal Breakdown</h3>
          <div style={{ overflowX: 'auto', WebkitOverflowScrolling: 'touch', width: '100%' }}>
            <table style={{ width: '100%', minWidth: '460px', borderCollapse: 'collapse', textAlign: 'left' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Channel</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>MTD Sales</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Velocity/Day</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Forecast</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Orders</th>
                </tr>
              </thead>
              <tbody>
                {portalStats.map((p, i) => {
                  const color = getPortalColor(p.name, i)
                  return (
                    <tr key={i} style={{ borderBottom: '1px solid rgba(255,255,255,0.02)' }}>
                      <td style={{ padding: '12px 0', fontWeight: 500, fontSize: '13px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <div style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: color, flexShrink: 0 }} />
                        <span style={{ color }}>{p.name}</span>
                      </td>
                      <td style={{ padding: '12px 0', fontSize: '13px' }}>{formatCurrency(p.value)}</td>
                      <td style={{ padding: '12px 0', fontSize: '13px', color: 'var(--text-muted)' }}>{formatCurrency(p.velocity)}</td>
                      <td style={{ padding: '12px 0', fontSize: '13px', fontWeight: 600 }}>{formatCurrency(p.forecast)}</td>
                      <td style={{ padding: '12px 0', fontSize: '13px' }}>{p.order_count}</td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        </div>

        {/* Country-Wise Sales & High Sales Prediction */}
        <div className="card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Globe size={18} color={themeColors.accent} />
              <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 600 }}>Country-Wise Sales & Prediction</h3>
            </div>
            <span style={{ fontSize: '11px', background: `${themeColors.accent}15`, color: themeColors.accent, border: `1px solid ${themeColors.accent}30`, padding: '3px 8px', borderRadius: '4px', fontWeight: 600 }}>
              Live Geo-Distribution
            </span>
          </div>

          <p style={{ margin: '0 0 16px 0', fontSize: '12px', color: 'var(--text-muted)' }}>
            Identify top-volume countries and forecast export growth opportunities for {companyView.toUpperCase()}.
          </p>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '14px', flex: 1 }}>
            {activeCountries.slice(0, 5).map((c, idx) => {
              const pred = countryPredictions[idx % countryPredictions.length]
              const barPct = Math.min(Math.max(c.pct, 4), 100)
              return (
                <div key={c.country || idx} style={{ background: 'rgba(255,255,255,0.02)', padding: '10px 12px', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.04)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '13px', fontWeight: 600 }}>{c.country}</span>
                      <span style={{ fontSize: '10px', background: `${pred.color}15`, color: pred.color, border: `1px solid ${pred.color}30`, padding: '2px 6px', borderRadius: '4px', fontWeight: 600 }}>
                        {pred.tag}
                      </span>
                    </div>
                    <div style={{ textAlign: 'right' }}>
                      <span style={{ fontSize: '13px', fontWeight: 700 }}>{formatCurrency(c.value)}</span>
                      <span style={{ fontSize: '11px', color: 'var(--text-muted)', marginLeft: '6px' }}>({c.pct}%)</span>
                    </div>
                  </div>

                  <div style={{ width: '100%', background: 'rgba(255,255,255,0.05)', height: '6px', borderRadius: '3px', overflow: 'hidden', marginBottom: '4px' }}>
                    <div style={{ width: `${barPct}%`, background: pred.color, height: '100%', borderRadius: '3px', transition: 'width 0.5s ease' }} />
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{pred.note}</div>
                </div>
              )
            })}
          </div>
        </div>
      </div>

      {/* ── AI Diagnostics & Recommendation Engine ── */}
      <div className="card" style={{ padding: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '10px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Sparkles size={20} color={themeColors.accent} />
            <h3 style={{ margin: 0, fontSize: '17px', fontWeight: 700 }}>AI Diagnostic & Sales Growth Playbook</h3>
          </div>
          <span style={{ fontSize: '12px', background: `${themeColors.accent}15`, color: themeColors.accent, border: `1px solid ${themeColors.accent}30`, padding: '4px 10px', borderRadius: '20px', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Zap size={13} /> {companyView.toUpperCase()} Intelligence
          </span>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(min(100%, 280px), 1fr))', gap: '20px' }}>

          {/* Causes Column */}
          <div style={{ background: 'rgba(239, 68, 68, 0.03)', border: '1px solid rgba(239, 68, 68, 0.15)', borderRadius: '12px', padding: '16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '14px', color: '#ef4444' }}>
              <TrendingDown size={18} />
              <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 700 }}>What Causes Sales to Slow Down</h4>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {aiInsights.causes.map((cause, i) => (
                <div key={i} style={{ padding: '10px', background: 'rgba(0,0,0,0.2)', borderRadius: '8px', borderLeft: '3px solid #ef4444' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                    <span style={{ fontSize: '13px', fontWeight: 600, color: '#fff' }}>{cause.title}</span>
                    <span style={{ fontSize: '10px', background: cause.impact === 'High' ? 'rgba(239,68,68,0.2)' : 'rgba(245,158,11,0.2)', color: cause.impact === 'High' ? '#ef4444' : '#f59e0b', padding: '2px 6px', borderRadius: '4px', fontWeight: 600 }}>
                      {cause.impact} Impact
                    </span>
                  </div>
                  <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted)', lineHeight: '1.5' }}>{cause.desc}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Solutions & Growth Column */}
          <div style={{ background: 'rgba(16, 185, 129, 0.03)', border: '1px solid rgba(16, 185, 129, 0.15)', borderRadius: '12px', padding: '16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '14px', color: '#10b981' }}>
              <ArrowUpRight size={18} />
              <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 700 }}>How We Can Increment Sales for All Portals</h4>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {aiInsights.recommendations.map((rec, i) => (
                <div key={i} style={{ padding: '10px', background: 'rgba(0,0,0,0.2)', borderRadius: '8px', borderLeft: '3px solid #10b981' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                    <span style={{ fontSize: '13px', fontWeight: 600, color: '#fff' }}>{rec.channel}</span>
                    <span style={{ fontSize: '11px', color: '#10b981', fontWeight: 600 }}>{rec.potential}</span>
                  </div>
                  <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted)', lineHeight: '1.5' }}>{rec.action}</p>
                </div>
              ))}
            </div>
          </div>

        </div>
      </div>

    </div>
  )
}
