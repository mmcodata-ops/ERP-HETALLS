import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove main fetchAll interval
content = re.sub(r'const interval = setInterval\(\(\) => fetchAll\(false\), 5000\);\n', '', content)
content = re.sub(r'clearInterval\(interval\);\n', '', content)

# Remove breakdown interval
breakdown_pattern = r'    let interval;\n    if \(showBreakdown\) \{\n      interval = setInterval\(\(\) => \{\n        let url = bdTab;\n        if \(bdTab === \'custom\'\) \{\n          url = bdCustomDate;\n          if \(bdCustomEndDate\) url \+= \|\$\{bdCustomEndDate\};\n        \}\n        axios\.get\(\$\{API\}/api/breakdown/\$\{url\}\)\.then\(res => setBdData\(res\.data\)\)\.catch\(console\.error\);\n      \}, 5000\);\n    \}\n\n    return \(\) => clearInterval\((interval|bdInterval)\);\n'

# Just comment out the breakdown interval to be safe and simple:
content = re.sub(
    r'      interval = setInterval\(\(\) => \{',
    r'      // removed interval = setInterval(() => {',
    content
)
content = re.sub(
    r'      \}, 5000\);',
    r'      // }, 5000);',
    content
)


with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
