import re

with open('Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove it from inside Dashboard
content = content.replace('''  const portalColorsMap = {
    "AMAZON": "#f59e0b",
    "CASAVANI WEBSITE": "#10b981",
    "EBAY-RUGSFOREVER": "#8b5cf6",
    "ETSY-CASAVANI": "#f43f5e",
    "ETSY-RUGSFOREVER": "#3b82f6",
    "JAYPOR": "#d946ef",
    "MIRRAW": "#06b6d4",
    "PEPPERFRY": "#84cc16",
    "WALMART": "#14b8a6",
    "EBAY-CASAVANI": "#eab308",
    "ETSY-MKM": "#ef4444",
    "EBAY-MKM": "#0ea5e9",
    "CRAFT-MKM": "#f97316",
    "EBAY-CASAVANI (CARPET)": "#fef08a",
    "AMAZON (CARPET)": "#fde68a",
    "ETSY-CASAVANI (CARPET)": "#fecaca",
    "ETSY-RUGSFOREVER (CARPET)": "#bfdbfe"
  };
  const fallbackColors = ["#6366f1", "#14b8a6", "#f43f5e", "#84cc16", "#d946ef", "#eab308", "#0ea5e9", "#f97316", "#a855f7"];
  const getPortalColor = (portal, index) => {
    return portalColorsMap[portal] || fallbackColors[index % fallbackColors.length];
  };''', '')

# 2. Add it to the top of the file after imports
imports_end = content.find('import', content.rfind('import')) # Find last import
imports_end = content.find('\\n', imports_end) + 1

global_vars = '''
export const PORTAL_COLORS_MAP = {
  "AMAZON": "#f59e0b",
  "CASAVANI WEBSITE": "#10b981",
  "EBAY-RUGSFOREVER": "#8b5cf6",
  "ETSY-CASAVANI": "#f43f5e",
  "ETSY-RUGSFOREVER": "#3b82f6",
  "JAYPOR": "#d946ef",
  "MIRRAW": "#06b6d4",
  "PEPPERFRY": "#84cc16",
  "WALMART": "#14b8a6",
  "EBAY-CASAVANI": "#eab308",
  "ETSY-MKM": "#ef4444",
  "EBAY-MKM": "#0ea5e9",
  "CRAFT-MKM": "#f97316",
  "EBAY-CASAVANI (CARPET)": "#fef08a",
  "AMAZON (CARPET)": "#fde68a",
  "ETSY-CASAVANI (CARPET)": "#fecaca",
  "ETSY-RUGSFOREVER (CARPET)": "#bfdbfe"
};
export const FALLBACK_COLORS = ["#6366f1", "#14b8a6", "#f43f5e", "#84cc16", "#d946ef", "#eab308", "#0ea5e9", "#f97316", "#a855f7"];
export const getPortalColor = (portal, index = 0) => {
  return PORTAL_COLORS_MAP[portal] || FALLBACK_COLORS[index % FALLBACK_COLORS.length];
};
'''

content = content[:imports_end] + global_vars + content[imports_end:]

# 3. Replace the popup color logic to use getPortalColor
content = content.replace('''<span style={{ color: c.color, fontWeight: 500 }}>{c.name}</span>''', '''<span style={{ color: getPortalColor(c.name, 0), fontWeight: 500 }}>{c.name}</span>''')

# 4. Replace the old getPortalColor usages in Dashboard component to use the global one.
# Wait, since I deleted the local definition, it will just use the global one seamlessly.

with open('Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
