import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add state for fullScreenChart
state_code = "const [chartView, setChartView] = useState('hg')"
if "fullScreenChart" not in code:
    code = code.replace(state_code, state_code + "\n  const [fullScreenChart, setFullScreenChart] = useState(null)")

# 2. Wrap PieChart
old_pie = """            {companiesRev?.today && companiesRev.today.length > 0 ? (() => {
              const pieData = chartView === 'ho'
                ? companiesRev.today.filter(c => c.name?.toUpperCase().includes('HETALLS'))
                : companiesRev.today.filter(c => !c.name?.toUpperCase().includes('HETALLS'));
              return pieData.length > 0 ? (
              <ResponsiveContainer width="100%" height={320}>"""

new_pie = """            {companiesRev?.today && companiesRev.today.length > 0 ? (() => {
              const pieData = chartView === 'ho'
                ? companiesRev.today.filter(c => c.name?.toUpperCase().includes('HETALLS'))
                : companiesRev.today.filter(c => !c.name?.toUpperCase().includes('HETALLS'));
              return pieData.length > 0 ? (
              <div onClick={() => { if (window.innerWidth <= 900) setFullScreenChart('pie'); }} style={{ cursor: window.innerWidth <= 900 ? 'pointer' : 'default', width: '100%' }}>
              <ResponsiveContainer width="100%" height={320}>"""

if old_pie in code:
    code = code.replace(old_pie, new_pie)

old_pie_close = """                </PieChart>
              </ResponsiveContainer>
            ) : ("""

new_pie_close = """                </PieChart>
              </ResponsiveContainer>
              </div>
            ) : ("""

if old_pie_close in code:
    code = code.replace(old_pie_close, new_pie_close)

# 3. Wrap ComposedChart
old_comp = """            <ResponsiveContainer width="100%" height={400}>
              <ComposedChart"""

new_comp = """            <div onClick={() => { if (window.innerWidth <= 900) setFullScreenChart('revenue'); }} style={{ cursor: window.innerWidth <= 900 ? 'pointer' : 'default', width: '100%' }}>
            <ResponsiveContainer width="100%" height={400}>
              <ComposedChart"""

if old_comp in code:
    code = code.replace(old_comp, new_comp)

old_comp_close = """              </ComposedChart>
            </ResponsiveContainer>
          </div>
        </div>"""

new_comp_close = """              </ComposedChart>
            </ResponsiveContainer>
            </div>
          </div>
        </div>"""

if old_comp_close in code:
    code = code.replace(old_comp_close, new_comp_close)


# 4. Add the Modal JSX at the very end of the component return
modal_jsx = """
      {/* Mobile Full Screen Chart Modal */}
      {fullScreenChart && (
        <div className="breakdown-overlay" onClick={() => setFullScreenChart(null)} style={{ zIndex: 10001, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="breakdown-modal" onClick={e => e.stopPropagation()} style={{ width: '95vw', height: '90vh', padding: '20px', position: 'relative', display: 'flex', flexDirection: 'column' }}>
            <button className="close-btn" onClick={() => setFullScreenChart(null)} style={{ position: 'absolute', top: 10, right: 10, background: 'none', border: 'none', color: '#fff', fontSize: '24px', cursor: 'pointer', zIndex: 10002 }}>&times;</button>
            <h3 style={{ fontSize: '16px', fontWeight: 700, margin: '0 0 16px 0', paddingRight: '20px' }}>
              {fullScreenChart === 'pie' ? "Today's Sales Distribution" : "Monthly Revenue Trend"}
            </h3>
            <div style={{ flex: 1, minHeight: 0, width: '100%' }}>
              {fullScreenChart === 'pie' ? (() => {
                const pieData = chartView === 'ho'
                  ? companiesRev.today.filter(c => c.name?.toUpperCase().includes('HETALLS'))
                  : companiesRev.today.filter(c => !c.name?.toUpperCase().includes('HETALLS'));
                return (
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart margin={{ top: 0, right: 0, bottom: 0, left: 0 }}>
                      <Pie isAnimationActive={false} data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={70} outerRadius={110} paddingAngle={5} stroke="none">
                        {pieData.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={getPortalColor(entry.name, index)} />
                        ))}
                      </Pie>
                      <Tooltip content={<CustomPieTooltip />} />
                      <Legend align="center" wrapperStyle={{ fontSize: 12, paddingTop: '10px' }} />
                    </PieChart>
                  </ResponsiveContainer>
                );
              })() : (
                <ResponsiveContainer width="100%" height="100%">
                  <ComposedChart data={revenueChart || []} margin={{ top: 15, right: 20, left: 0, bottom: 0 }} maxBarSize={45} onClick={() => setTooltipLocked(!tooltipLocked)}>
                    <CartesianGrid stroke="var(--border)" strokeDasharray="3 3" vertical={false} />
                    <XAxis dataKey="month" tick={{ fill: 'var(--text-muted)', fontSize: 11 }} axisLine={false} tickLine={false} />
                    <YAxis yAxisId="left" tick={{ fill: 'var(--text-muted)', fontSize: 11 }} axisLine={false} tickLine={false} tickFormatter={v => `$${v/1000}k`} />
                    <YAxis yAxisId="right" orientation="right" tick={{ fill: '#ef4444', fontSize: 11 }} axisLine={false} tickLine={false} label={{ value: 'Sales', angle: -90, position: 'right', fill: '#ef4444', fontSize: 11, fontWeight: 600, offset: 5 }} />
                    <Tooltip content={<ProgressChartTooltip data={revenueChart} hoveredDataKey={hoveredDataKey} tooltipLocked={tooltipLocked} chartView={chartView} />} cursor={false} position={{ y: 0 }} wrapperStyle={{ zIndex: 100 }} />
                    <Legend align="center" verticalAlign="bottom" wrapperStyle={{ fontSize: 12, paddingTop: '12px' }} />
                    {allChartPortals.filter(portal => chartView === 'ho' ? portal.toUpperCase().includes('HETALLS') : !portal.toUpperCase().includes('HETALLS')).map((portal, idx) => (
                      <Bar isAnimationActive={false} yAxisId="left" key={portal} dataKey={portal} name={formatPortalName(portal)} fill={getPortalColor(portal, idx)} stackId="a" onMouseEnter={() => setHoveredDataKey(portal)} onMouseLeave={() => setHoveredDataKey(null)} />
                    ))}
                    <Line isAnimationActive={false} yAxisId="right" type="linear" dataKey={chartView === 'ho' ? 'order_count_ho' : 'order_count_hg'} name="Sales Count" legendType="none" stroke="#ef4444" strokeWidth={1} label={{ position: 'top', offset: 12, fill: '#ef4444', fontSize: 12, fontWeight: 500 }} dot={{ r: 4, fill: '#ef4444', stroke: '#fff', strokeWidth: 1.5 }} activeDot={{ r: 6, fill: '#ef4444', stroke: '#fff' }} />
                  </ComposedChart>
                </ResponsiveContainer>
              )}
            </div>
          </div>
        </div>
      )}
"""

if modal_jsx not in code:
    code = code.replace("    )\n  }\n", modal_jsx + "    )\n  }\n")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Added chart full-screen modal feature for mobile")
