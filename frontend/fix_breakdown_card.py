import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_code = """    <div key="breakdown" onClick={openBreakdown} style={{ cursor: 'pointer', display: 'flex', flexDirection: 'column', flex: 1 }}>
      <KPICard icon={Layers} label="Detailed Breakdown" value="Breakdown" sub="Daily Sale Brands & Portal" colorClass="blue" format="text" className="h-full" />
    </div>"""

new_code = """    <div key="breakdown" onClick={openBreakdown} className="cube-container" style={{ cursor: 'pointer' }}>
      <div className="cube-face" style={{ position: 'relative', transform: 'none' }}>
        <div style={{ width: '100%', height: '100%' }}>
          <KPICard icon={Layers} label="Detailed Breakdown" value="Breakdown" sub="Daily Sale Brands & Portal" colorClass="blue" format="text" />
        </div>
      </div>
    </div>"""

if old_code in code:
    code = code.replace(old_code, new_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Successfully replaced Detailed Breakdown card markup!")
else:
    print("Could not find exact old_code block. Attempting regex...")
    old_regex = r"<div key=\"breakdown\"[^>]*>\s*<KPICard icon=\{Layers\}[^>]*/>\s*</div>"
    if re.search(old_regex, code):
        code = re.sub(old_regex, new_code, code)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        print("Successfully replaced Detailed Breakdown card markup using regex!")
    else:
        print("FAILED to find Detailed Breakdown card markup.")
