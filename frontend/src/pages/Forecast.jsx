import React, { useState, useEffect } from 'react'
import axios from 'axios'
import {
  TrendingUp, Target, Activity, CheckCircle, Clock, AlertTriangle, AlertCircle, DollarSign
} from 'lucide-react'
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine, Cell
} from 'recharts'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function Forecast() {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)
  const [targetStr, setTargetStr] = useState(localStorage.getItem('forecast_target') || '100000')
  const [isEditingTarget, setIsEditingTarget] = useState(false)

  const target = parseFloat(targetStr) || 0

  useEffect(() => {
    let isMounted = true
    axios.get(`${API}/api/dashboard/companies-revenue`)
      .then(res => {
        if (isMounted && res.data && res.data.month) {
          setData(res.data.month)
        }
      })
      .finally(() => {
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
  const daysPassed = today.getDate()
  const totalDays = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate()
  const daysRemaining = Math.max(totalDays - daysPassed, 1)

  const mtdSales = data.reduce((acc, curr) => acc + curr.value, 0)
  const salesVelocity = mtdSales / (daysPassed || 1)
  const forecast = salesVelocity * totalDays
  
  const salesGap = Math.max(target - mtdSales, 0)
  const requiredVelocity = salesGap > 0 ? salesGap / daysRemaining : 0
  const targetAchieve = target > 0 ? (mtdSales / target) * 100 : 0
  
  let confidence = 'Low'
  let confColor = 'var(--danger-color)'
  if (forecast >= target) {
     confidence = 'High'
     confColor = 'var(--success-color)'
  } else if (forecast >= target * 0.85) {
     confidence = 'Medium'
     confColor = 'var(--warning-color)'
  }

  const portalStats = data.map(p => {
     const vel = p.value / (daysPassed || 1)
     const pFor = vel * totalDays
     return { ...p, velocity: vel, forecast: pFor }
  }).sort((a,b) => b.forecast - a.forecast)

  const formatCurrency = (val) => `$${val.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`

  const chartData = [
    { name: 'MTD Sales', value: mtdSales, color: '#3b82f6' },
    { name: 'Forecast', value: forecast, color: confColor }
  ]

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div style={{ background: 'rgba(10, 15, 30, 0.95)', border: '1px solid var(--border-color)', padding: '12px', borderRadius: '8px', color: '#fff' }}>
          <p style={{ margin: '0 0 8px 0', fontWeight: 'bold' }}>{label}</p>
          <p style={{ margin: 0, color: payload[0].payload.color }}>
            {formatCurrency(payload[0].value)}
          </p>
        </div>
      );
    }
    return null;
  };

  if (loading) {
    return <div className="p-8" style={{ color: 'var(--text-muted)' }}>Loading forecast data...</div>
  }

  return (
    <div className="dashboard" style={{ padding: '24px', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
        <div>
          <h1 style={{ fontSize: '24px', fontWeight: 700, margin: '0 0 4px 0' }}>Month End Sales Forecast</h1>
          <p style={{ margin: 0, color: 'var(--text-muted)' }}>Projecting month-end performance based on MTD sales.</p>
        </div>
        <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
          <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
            Day {daysPassed} of {totalDays}
          </div>
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

      {/* KPI Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px', marginBottom: '24px' }}>
        <div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>MTD Sales</span>
            <DollarSign size={18} color="#3b82f6" />
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px' }}>{formatCurrency(mtdSales)}</div>
          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Current month to date</div>
        </div>

        <div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Forecast</span>
            <TrendingUp size={18} color={confColor} />
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px', color: confColor }}>{formatCurrency(forecast)}</div>
          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Projected month end</div>
        </div>

        <div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Target Achieved</span>
            <CheckCircle size={18} color={targetAchieve >= 100 ? "var(--success-color)" : "var(--primary-color)"} />
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px' }}>{targetAchieve.toFixed(1)}%</div>
          <div style={{ width: '100%', background: 'rgba(255,255,255,0.1)', height: '4px', borderRadius: '2px', marginTop: '8px' }}>
            <div style={{ width: `${Math.min(targetAchieve, 100)}%`, background: targetAchieve >= 100 ? 'var(--success-color)' : 'var(--primary-color)', height: '100%', borderRadius: '2px' }} />
          </div>
        </div>

        <div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Confidence</span>
            {confidence === 'High' ? <CheckCircle size={18} color={confColor} /> : 
             confidence === 'Medium' ? <AlertCircle size={18} color={confColor} /> : 
             <AlertTriangle size={18} color={confColor} />}
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px', color: confColor }}>{confidence}</div>
          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>To hit monthly target</div>
        </div>
      </div>

      {/* Velocity and Gap */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '24px', marginBottom: '24px' }}>
        <div className="card" style={{ padding: '24px' }}>
          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Activity size={18} color="var(--primary-color)" />
            Velocity & Gap Analysis
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '12px', borderBottom: '1px solid var(--border-color)' }}>
              <div>
                <div style={{ fontSize: '14px', fontWeight: 500 }}>Sales Velocity</div>
                <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Average per day</div>
              </div>
              <div style={{ fontSize: '18px', fontWeight: 600 }}>{formatCurrency(salesVelocity)}/day</div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '12px', borderBottom: '1px solid var(--border-color)' }}>
              <div>
                <div style={{ fontSize: '14px', fontWeight: 500 }}>Sales Gap</div>
                <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Remaining to hit target</div>
              </div>
              <div style={{ fontSize: '18px', fontWeight: 600, color: 'var(--warning-color)' }}>{formatCurrency(salesGap)}</div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <div style={{ fontSize: '14px', fontWeight: 500 }}>Required Velocity</div>
                <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Required per day to hit target</div>
              </div>
              <div style={{ fontSize: '18px', fontWeight: 600, color: requiredVelocity > salesVelocity ? 'var(--danger-color)' : 'var(--success-color)' }}>
                {formatCurrency(requiredVelocity)}/day
              </div>
            </div>
          </div>
        </div>

        <div className="card" style={{ padding: '24px', height: '300px' }}>
          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 600 }}>Overall Trajectory</h3>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
              <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)' }} />
              <YAxis tickFormatter={v => `$${v/1000}k`} axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)' }} />
              <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(255,255,255,0.05)' }} />
              <ReferenceLine y={target} stroke="var(--primary-color)" strokeDasharray="3 3" label={{ position: 'top', value: 'Target', fill: 'var(--primary-color)', fontSize: 12 }} />
              <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                {chartData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Portals Table */}
      <div className="card">
        <div className="card-header">
          <h2 className="card-title">Portal Forecast Breakdown</h2>
          <p className="card-subtitle">Projected performance by individual sales channels</p>
        </div>
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
            <thead>
              <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
                <th style={{ padding: '16px', color: 'var(--text-muted)', fontWeight: 500, fontSize: '13px' }}>Portal</th>
                <th style={{ padding: '16px', color: 'var(--text-muted)', fontWeight: 500, fontSize: '13px' }}>MTD Sales</th>
                <th style={{ padding: '16px', color: 'var(--text-muted)', fontWeight: 500, fontSize: '13px' }}>Velocity/Day</th>
                <th style={{ padding: '16px', color: 'var(--text-muted)', fontWeight: 500, fontSize: '13px' }}>Forecast</th>
                <th style={{ padding: '16px', color: 'var(--text-muted)', fontWeight: 500, fontSize: '13px' }}>Orders (MTD)</th>
              </tr>
            </thead>
            <tbody>
              {portalStats.map((p, i) => (
                <tr key={i} style={{ borderBottom: '1px solid rgba(255,255,255,0.02)' }}>
                  <td style={{ padding: '16px', fontWeight: 500, display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <div style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: p.color || '#3b82f6' }} />
                    {p.name}
                  </td>
                  <td style={{ padding: '16px' }}>{formatCurrency(p.value)}</td>
                  <td style={{ padding: '16px', color: 'var(--text-muted)' }}>{formatCurrency(p.velocity)}</td>
                  <td style={{ padding: '16px', fontWeight: 600 }}>{formatCurrency(p.forecast)}</td>
                  <td style={{ padding: '16px' }}>{p.order_count}</td>
                </tr>
              ))}
              {portalStats.length === 0 && (
                <tr>
                  <td colSpan={5} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>
                    No portal data available for this month.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  )
}
