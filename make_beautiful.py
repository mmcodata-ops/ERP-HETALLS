import os

file_path = 'frontend/src/pages/Forecast.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the equiv bug
content = content.replace(
    "!['month', 'order_count_hg', 'order_count_ho', '_dt'].includes(key)",
    "!['month', 'order_count_hg', 'order_count_ho', '_dt', 'equiv'].includes(key)"
)
# Ensure we parse float
content = content.replace(
    "dayTotal += (dayData[key] || 0)",
    "dayTotal += (parseFloat(dayData[key]) || 0)"
)
content = content.replace(
    "if (pKey) dayTotal += dayData[pKey];",
    "if (pKey) dayTotal += (parseFloat(dayData[pKey]) || 0);"
)
content = content.replace(
    "dayTotal += dayData[selectedPortal];",
    "dayTotal += (parseFloat(dayData[selectedPortal]) || 0);"
)

# Convert LineChart to AreaChart
content = content.replace(
    "import {\n  LineChart, Line",
    "import {\n  AreaChart, Area, ComposedChart, Line"
)
content = content.replace("<LineChart", "<ComposedChart")
content = content.replace("</LineChart>", "</ComposedChart>")

chart_gradient = """          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 600 }}>Cumulative MTD Sales vs Target Trajectory</h3>
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart data={chartData} margin={{ top: 10, right: 30, left: 20, bottom: 5 }}>
              <defs>
                <linearGradient id="colorActual" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.4}/>
                  <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
              <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)', fontSize: 12 }} />
              <YAxis tickFormatter={v => `$${v/1000}k`} axisLine={false} tickLine={false} tick={{ fill: 'var(--text-muted)', fontSize: 12 }} />
              <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(255,255,255,0.05)' }} />
              <Legend wrapperStyle={{ fontSize: 13, paddingTop: '10px' }} />
              <Area 
                type="linear" 
                dataKey="Actual Sales" 
                stroke="#3b82f6" 
                fillOpacity={1} 
                fill="url(#colorActual)" 
                strokeWidth={3} 
                isAnimationActive={false}
                dot={{ r: 4, strokeWidth: 2, fill: '#3b82f6', stroke: '#1a1f36' }} 
                activeDot={{ r: 6 }} 
              />
              <Line 
                type="linear" 
                dataKey="Target Trajectory" 
                stroke="#10b981" 
                strokeWidth={3} 
                isAnimationActive={false}
                strokeDasharray="5 5"
                dot={{ r: 4, strokeWidth: 2, fill: '#10b981', stroke: '#1a1f36' }} 
                activeDot={{ r: 6 }} 
              />
            </ComposedChart>"""
            
# Find the exact LineChart block to replace
start_idx = content.find("<h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 600 }}>Cumulative MTD Sales vs Target Trajectory</h3>")
end_idx = content.find("</ResponsiveContainer>", start_idx) + len("</ResponsiveContainer>")
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + chart_gradient + content[end_idx:]

# Style the KPI Cards
# MTD Sales Card
mtd_card_old = """<div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>MTD Sales</span>
            <DollarSign size={18} color="var(--primary-color)" />
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px' }}>{formatCurrency(mtdSales)}</div>
          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Current month to date</div>
        </div>"""
mtd_card_new = """<div className="card" style={{ padding: '20px', background: 'linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(30,58,138,0.05) 100%)', border: '1px solid rgba(59,130,246,0.2)', boxShadow: '0 4px 20px rgba(59,130,246,0.05)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '14px', fontWeight: 500 }}>MTD Sales</span>
            <div style={{ background: 'rgba(59,130,246,0.2)', padding: '6px', borderRadius: '8px' }}>
              <DollarSign size={18} color="#3b82f6" />
            </div>
          </div>
          <div style={{ fontSize: '28px', fontWeight: 800, marginBottom: '4px', background: 'linear-gradient(to right, #60a5fa, #3b82f6)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>{formatCurrency(mtdSales)}</div>
          <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Current month to date</div>
        </div>"""
content = content.replace(mtd_card_old, mtd_card_new)

# Forecast Card
forecast_card_old = """<div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Forecast</span>
            <TrendingUp size={18} color={confColor} />
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px', color: confColor }}>{formatCurrency(forecast)}</div>
          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Projected month end</div>
        </div>"""
forecast_card_new = """<div className="card" style={{ padding: '20px', background: `linear-gradient(135deg, ${confColor}15 0%, rgba(0,0,0,0) 100%)`, border: `1px solid ${confColor}30`, boxShadow: `0 4px 20px ${confColor}10` }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '14px', fontWeight: 500 }}>Forecast</span>
            <div style={{ background: `${confColor}20`, padding: '6px', borderRadius: '8px' }}>
              <TrendingUp size={18} color={confColor} />
            </div>
          </div>
          <div style={{ fontSize: '28px', fontWeight: 800, marginBottom: '4px', color: confColor }}>{formatCurrency(forecast)}</div>
          <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Projected month end</div>
        </div>"""
content = content.replace(forecast_card_old, forecast_card_new)

# Target Achieved Card
target_card_old = """<div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Target Achieved</span>
            <CheckCircle size={18} color={targetAchieve >= 100 ? "var(--success-color)" : "var(--primary-color)"} />
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px' }}>{targetAchieve.toFixed(1)}%</div>
          <div style={{ width: '100%', background: 'rgba(255,255,255,0.1)', height: '4px', borderRadius: '2px', marginTop: '8px' }}>
            <div style={{ width: `${Math.min(targetAchieve, 100)}%`, background: targetAchieve >= 100 ? 'var(--success-color)' : 'var(--primary-color)', height: '100%', borderRadius: '2px' }} />
          </div>
        </div>"""
target_card_new = """<div className="card" style={{ padding: '20px', background: targetAchieve >= 100 ? 'linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(6,78,59,0.05) 100%)' : 'var(--surface-color)', border: targetAchieve >= 100 ? '1px solid rgba(16,185,129,0.2)' : '1px solid var(--border-color)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '14px', fontWeight: 500 }}>Target Achieved</span>
            <div style={{ background: targetAchieve >= 100 ? 'rgba(16,185,129,0.2)' : 'rgba(59,130,246,0.2)', padding: '6px', borderRadius: '8px' }}>
              <CheckCircle size={18} color={targetAchieve >= 100 ? "#10b981" : "#3b82f6"} />
            </div>
          </div>
          <div style={{ fontSize: '28px', fontWeight: 800, marginBottom: '4px', color: targetAchieve >= 100 ? '#10b981' : '#fff' }}>{targetAchieve.toFixed(1)}%</div>
          <div style={{ width: '100%', background: 'rgba(255,255,255,0.1)', height: '6px', borderRadius: '3px', marginTop: '12px', overflow: 'hidden' }}>
            <div style={{ width: `${Math.min(targetAchieve, 100)}%`, background: targetAchieve >= 100 ? '#10b981' : 'linear-gradient(90deg, #3b82f6, #60a5fa)', height: '100%', borderRadius: '3px', transition: 'width 0.5s ease' }} />
          </div>
        </div>"""
content = content.replace(target_card_old, target_card_new)

# Confidence Card
conf_card_old = """<div className="card" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Confidence</span>
            {confidence === 'High' ? <CheckCircle size={18} color={confColor} /> : 
             confidence === 'Medium' ? <AlertCircle size={18} color={confColor} /> : 
             <AlertTriangle size={18} color={confColor} />}
          </div>
          <div style={{ fontSize: '24px', fontWeight: 700, marginBottom: '4px', color: confColor }}>{confidence}</div>
          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>To hit monthly target</div>
        </div>"""
conf_card_new = """<div className="card" style={{ padding: '20px', background: `linear-gradient(135deg, ${confColor}10 0%, rgba(0,0,0,0) 100%)`, border: `1px solid ${confColor}25` }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '14px', fontWeight: 500 }}>Confidence</span>
            <div style={{ background: `${confColor}20`, padding: '6px', borderRadius: '8px' }}>
              {confidence === 'High' ? <CheckCircle size={18} color={confColor} /> : 
               confidence === 'Medium' ? <AlertCircle size={18} color={confColor} /> : 
               <AlertTriangle size={18} color={confColor} />}
            </div>
          </div>
          <div style={{ fontSize: '28px', fontWeight: 800, marginBottom: '4px', color: confColor }}>{confidence}</div>
          <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>To hit monthly target</div>
        </div>"""
content = content.replace(conf_card_old, conf_card_new)

# Style the dropdown slightly better
content = content.replace("outline: 'none'", "outline: 'none', fontWeight: 600, fontSize: '14px', cursor: 'pointer'")

# Replace confColor to be hex codes to be completely safe in templates
content = content.replace("confColor = 'var(--danger-color)'", "confColor = '#ef4444'")
content = content.replace("confColor = 'var(--success-color)'", "confColor = '#10b981'")
content = content.replace("confColor = 'var(--warning-color)'", "confColor = '#f59e0b'")


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Make beautiful")
