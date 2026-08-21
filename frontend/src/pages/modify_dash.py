import re

with open('Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('''  const portalColorsMap = {
    "AMAZON": "#f59e0b",
    "CASAVANI WEBSITE": "#10b981",
    "EBAY-RUGSFOREVER": "#8b5cf6",
    "ETSY-CASAVANI": "#f43f5e",
    "ETSY-RUGSFOREVER": "#3b82f6",
    "JAYPOR": "#d946ef",
    "MIRRAW": "#06b6d4",
    "PEPPERFRY": "#84cc16",
    "WALMART": "#14b8a6"
  };''', '''  const portalColorsMap = {
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
  };''')

with open('Dashboard.jsx', 'w', encoding='utf-8') as f:
    f.write(content)
