import os

file_path = 'frontend/src/pages/Forecast.jsx'

jsx_content = """import React, { useState, useEffect } from 'react'
import axios from 'axios'
import {
  TrendingUp, Target, Activity, CheckCircle, Clock, AlertTriangle, AlertCircle, DollarSign
} from 'lucide-react'
import {
  AreaChart, Area, ComposedChart, Line, BarChart, Bar, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function Forecast() {
  const [portalData, setPortalData] = useState([])
  const [dailyData, setDailyData] = useState([])
  const [loading, setLoading] = useState(true)
  const [targetStr, setTargetStr] = useState(localStorage.getItem('forecast_target') || '100000')
  const [isEditingTarget, setIsEditingTarget] = useState(false)
  const [selectedPortal, setSelectedPortal] = useState('All')

  const target = parseFloat(targetStr) || 0

  useEffect(() => {
    let isMounted = true
    Promise.all([
      axios.get(`${API}/api/dashboard/companies-revenue`),
      axios.get(`${API}/api/dashboard/revenue-chart?group_by=day`)
    ]).then(([compRes, dailyRes]) => {
      if (isMounted) {
        if (compRes.data && compRes.data.month) {
          setPortalData(compRes.data.month)
        }
        if (dailyRes.data) {
          setDailyData(dailyRes.data)
        }
      }
    }).finally(() => {
      if (isMounted) setLoading(false)
    })
    return () => { isMounted = false }
  }, [])

  const handleTargetChange = (e) => {
    setTargetStr(e.target.value)
  }

  const handleTargetSave = () => {
    localStorage.setItem('forecast_target', targetStr)
    setIsEditingTarget(false)
  }

  const today = new Date()
  const currentMonth = today.getMonth()
  const currentYear = today.getFullYear()
  const daysPassed = today.getDate()
  const totalDays = new Date(currentYear, currentMonth + 1, 0).getDate()
  const daysRemaining = Math.max(totalDays - daysPassed, 1)

  const filteredPortalData = portalData.filter(p => selectedPortal === 'All' || p.name === selectedPortal)
  const mtdSales = filteredPortalData.reduce((acc, curr) => acc + curr.value, 0)
  
  const salesVelocity = mtdSales / (daysPassed || 1)
  const forecast = salesVelocity * totalDays
  
  const salesGap = Math.max(target - mtdSales, 0)
  const requiredVelocity = salesGap > 0 ? salesGap / daysRemaining : 0
  const targetAchieve = target > 0 ? (mtdSales / target) * 100 : 0
  
  let confidence = 'Low'
  let confColor = '#ef4444' // danger
  if (forecast >= target) {
     confidence = 'High'
     confColor = '#10b981' // success
  } else if (forecast >= target * 0.85) {
     confidence = 'Medium'
     confColor = '#f59e0b' // warning
  }

  const portalStats = filteredPortalData.map(p => {
     const vel = p.value / (daysPassed || 1)
     const pFor = vel * totalDays
     return { ...p, velocity: vel, forecast: pFor }
  }).sort((a,b) => b.forecast - a.forecast)

  const formatCurrency = (val) => `$${(val || 0).toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`

  // Process daily data to create the line chart (Cumulative Actual vs Target Trajectory)
  let cumulative = 0
  const chartData = []
  
  const currentMonthData = dailyData
    .filter(d => d._dt && new Date(d._dt).getMonth() === currentMonth && new Date(d._dt).getFullYear() === currentYear)
    .sort((a, b) => new Date(a._dt) - new Date(b._dt))

  for (let i = 1; i <= daysPassed; i++) {
    const dateObj = new Date(currentYear, currentMonth, i)
    const dayLabel = dateObj.toLocaleDateString('en-GB', { day: '2-digit', month: 'short' })
    
    const dayData = currentMonthData.find(d => new Date(d._dt).getDate() === i)
    
    let dayTotal = 0
    if (dayData) {
      if (selectedPortal !== 'All') {
        if (dayData[selectedPortal]) {
           dayTotal += (parseFloat(dayData[selectedPortal]) || 0);
        } else {
           const pKey = Object.keys(dayData).find(k => k.toLowerCase() === selectedPortal.toLowerCase())
           if (pKey) dayTotal += (parseFloat(dayData[pKey]) || 0);
        }
      } else {
        Object.keys(dayData).forEach(key => {
          if (!['month', 'order_count_hg', 'order_count_ho', '_dt', 'equiv'].includes(key)) {
            dayTotal += (parseFloat(dayData[key]) || 0)
          }
        })
      }
    }
    
    cumulative += dayTotal
    const targetTrajectory = ((target || 0) / (totalDays || 1)) * i
    
    chartData.push({
      name: dayLabel,
      'Actual Sales': cumulative,
      'Target Trajectory': targetTrajectory
    })
  }

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div style={{ background: 'var(--surface-color)', border: '1px solid var(--border-color)', padding: '12px', borderRadius: '8px', color: '#fff', boxShadow: '0 4px 12px rgba(0,0,0,0.5)' }}>
          <p style={{ margin: '0 0 8px 0', fontWeight: 'bold' }}>{label}</p>
          {payload.map((p, idx) => (
             <p key={idx} style={{ margin: '0 0 4px 0', color: p.color, fontWeight: 500 }}>
               {p.name}: {formatCurrency(p.value)}
             </p>
          ))}
        </div>
      );
    }
    return null;
  };

  const CustomBarLabel = (props) => {
    const { x, y, width, height, value } = props;
    return (
      <text x={x + width + 10} y={y + height / 2} fill="var(--text-muted)" dy="0.35em" fontSize="12" fontWeight="500">
        {formatCurrency(value)}
      </text>
    );
  };

  if (loading) {
    return <div className="p-8" style={{ color: 'var(--text-muted)' }}>Loading forecast data...</div>
  }

  return (
    <div className="dashboard" style={{ padding: '24px', maxWidth: '1400px', margin: '0 auto' }}>
      
      {/* Header Area */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
        <div>
          <h1 style={{ fontSize: '24px', fontWeight: 700, margin: '0 0 4px 0' }}>Site Preview</h1>
          <p style={{ margin: 0, color: 'var(--text-muted)' }}>Projecting month-end performance for your sales channels.</p>
        </div>
        <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'var(--surface-color)', padding: '6px 12px', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
            <Target size={16} color="var(--primary-color)" />
            <span style={{ fontSize: '14px', color: 'var(--text-muted)' }}>Target:</span>
            {isEditingTarget ? (
              <div style={{ display: 'flex', gap: '8px' }}>
                <input 
                  type="number" 
                  value={targetStr} 
                  onChange={handleTargetChange}
                  style={{ width: '100px', background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border-color)', color: '#fff', borderRadius: '4px', padding: '2px 8px' }}
                />
                <button onClick={handleTargetSave} style={{ background: 'var(--primary-color)', border: 'none', color: '#fff', borderRadius: '4px', padding: '2px 8px', cursor: 'pointer' }}>Save</button>
              </div>
            ) : (
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                <span style={{ fontWeight: 600, fontSize: '15px' }}>{formatCurrency(target)}</span>
                <button onClick={() => setIsEditingTarget(true)} style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '12px', textDecoration: 'underline' }}>Edit</button>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* 6 Mini KPI Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px', marginBottom: '24px' }}>
        <div className="card" style={{ padding: '16px', borderLeft: '4px solid #3b82f6' }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>MTD Sales</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{formatCurrency(mtdSales)}</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${confColor}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Forecast</div>
          <div style={{ fontSize: '20px', fontWeight: 700, color: confColor }}>{formatCurrency(forecast)}</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${targetAchieve >= 100 ? '#10b981' : '#3b82f6'}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Target Achieved</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{targetAchieve.toFixed(1)}%</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: `4px solid ${confColor}` }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Confidence</div>
          <div style={{ fontSize: '20px', fontWeight: 700, color: confColor }}>{confidence}</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: '4px solid #f59e0b' }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Sales Velocity</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{formatCurrency(salesVelocity)}/d</div>
        </div>
        <div className="card" style={{ padding: '16px', borderLeft: '4px solid #ef4444' }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginBottom: '4px' }}>Sales Gap</div>
          <div style={{ fontSize: '20px', fontWeight: 700 }}>{formatCurrency(salesGap)}</div>
        </div>
      </div>

      {/* 2x2 Grid Layout matching user's design reference */}
      <div style={{ display: 'grid', gridTemplateColumns: '3fr 2fr', gap: '24px', marginBottom: '24px' }}>
        
        {/* Top Left: Sales Overview (Line Chart) */}
        <div className="card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 600 }}>Sales Overview</h3>
            <select 
              value={selectedPortal} 
              onChange={(e) => setSelectedPortal(e.target.value)} 
              style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid var(--border-color)', color: '#fff', borderRadius: '4px', padding: '6px 12px', outline: 'none', cursor: 'pointer', fontSize: '13px' }}
            >
              <option value="All">All Channels</option>
              {portalData.map(p => <option key={p.name} value={p.name}>{p.name}</option>)}
            </select>
          </div>
          <div style={{ flex: 1, minHeight: '300px' }}>
            <ResponsiveContainer width="100%" height="100%">
              <ComposedChart data={chartData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorActual" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.4}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)', fontSize: 11 }} />
                <YAxis tickFormatter={v => `$${v/1000}k`} axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)', fontSize: 11 }} width={50} />
                <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(255,255,255,0.05)' }} />
                <Legend wrapperStyle={{ fontSize: 12, paddingTop: '10px' }} />
                <Area type="linear" dataKey="Actual Sales" stroke="#3b82f6" fillOpacity={1} fill="url(#colorActual)" strokeWidth={3} isAnimationActive={false} dot={{ r: 4, strokeWidth: 2, fill: '#3b82f6', stroke: '#1a1f36' }} activeDot={{ r: 6 }} />
                <Line type="linear" dataKey="Target Trajectory" stroke="#10b981" strokeWidth={3} isAnimationActive={false} dot={{ r: 4, strokeWidth: 2, fill: '#10b981', stroke: '#1a1f36' }} activeDot={{ r: 6 }} />
              </ComposedChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Top Right: Sales by Source (Donut Chart) */}
        <div className="card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <h3 style={{ margin: '0 0 24px 0', fontSize: '16px', fontWeight: 600 }}>Sales by Source</h3>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
            <div style={{ width: '50%', height: '220px', position: 'relative' }}>
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie data={portalStats} dataKey="value" innerRadius={60} outerRadius={80} stroke="none" isAnimationActive={false}>
                    {portalStats.map((entry, index) => <Cell key={index} fill={entry.color || '#3b82f6'} />)}
                  </Pie>
                  <Tooltip formatter={(val) => formatCurrency(val)} contentStyle={{ background: 'var(--surface-color)', border: '1px solid var(--border-color)', borderRadius: '8px' }} />
                </PieChart>
              </ResponsiveContainer>
              <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', pointerEvents: 'none' }}>
                <span style={{ fontSize: '20px', fontWeight: 'bold' }}>{formatCurrency(mtdSales)}</span>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Total MTD</span>
              </div>
            </div>
            
            {/* Custom Legend */}
            <div style={{ width: '45%', display: 'flex', flexDirection: 'column', gap: '12px', maxHeight: '220px', overflowY: 'auto' }}>
              {portalStats.slice(0, 6).map(p => (
                <div key={p.name} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: '12px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', overflow: 'hidden' }}>
                    <div style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: p.color || '#3b82f6', flexShrink: 0 }} />
                    <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{p.name}</span>
                  </div>
                  <div style={{ fontWeight: 600, color: 'var(--text-muted)', marginLeft: '8px' }}>
                    {((p.value / (mtdSales || 1)) * 100).toFixed(0)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Bottom Left: Portal Forecast Breakdown (Table) */}
        <div className="card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 600 }}>Portal Breakdown</h3>
          <div style={{ overflowX: 'auto', flex: 1 }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Channel</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>MTD Sales</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Orders</th>
                  <th style={{ padding: '12px 0', color: 'var(--text-muted)', fontWeight: 500, fontSize: '12px' }}>Status</th>
                </tr>
              </thead>
              <tbody>
                {portalStats.map((p, i) => (
                  <tr key={i} style={{ borderBottom: '1px solid rgba(255,255,255,0.02)' }}>
                    <td style={{ padding: '12px 0', fontWeight: 500, fontSize: '13px' }}>{p.name}</td>
                    <td style={{ padding: '12px 0', fontSize: '13px' }}>{formatCurrency(p.value)}</td>
                    <td style={{ padding: '12px 0', fontSize: '13px', color: 'var(--text-muted)' }}>{p.order_count}</td>
                    <td style={{ padding: '12px 0' }}>
                      <span style={{ background: 'rgba(16,185,129,0.1)', color: '#10b981', padding: '4px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: 600 }}>Active</span>
                    </td>
                  </tr>
                ))}
                {portalStats.length === 0 && (
                  <tr>
                    <td colSpan={4} style={{ padding: '24px 0', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
                      No data available.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>

        {/* Bottom Right: Top Selling Channels (Horizontal Bar Chart) */}
        <div className="card" style={{ padding: '24px', display: 'flex', flexDirection: 'column' }}>
          <h3 style={{ margin: '0 0 24px 0', fontSize: '16px', fontWeight: 600 }}>Top Channels</h3>
          <div style={{ flex: 1, minHeight: '250px' }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={portalStats.slice(0, 5)} layout="vertical" margin={{ top: 0, right: 60, left: -20, bottom: 0 }} barSize={16}>
                <XAxis type="number" hide />
                <YAxis type="category" dataKey="name" axisLine={false} tickLine={false} width={120} tick={{ fill: 'var(--text-muted)', fontSize: 11 }} />
                <Tooltip cursor={{ fill: 'rgba(255,255,255,0.02)' }} contentStyle={{ background: 'var(--surface-color)', border: 'none', borderRadius: '8px' }} />
                <Bar dataKey="value" radius={[0, 4, 4, 0]} isAnimationActive={false} label={<CustomBarLabel />}>
                  {portalStats.slice(0, 5).map((entry, index) => (
                    <Cell key={index} fill={entry.color || '#3b82f6'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

      </div>
    </div>
  )
}
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(jsx_content)

print("Restructured Forecast.jsx perfectly to match design reference")
