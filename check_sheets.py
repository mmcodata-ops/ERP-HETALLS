import pandas as pd
url = "https://docs.google.com/spreadsheets/d/11NAw3BWNt3Bwcl1OqDv2EyL5WSLN1wZUg4qziq8SRDM/export?format=xlsx"
try:
    xl = pd.ExcelFile(url)
    print("Sheets in CARPET:", xl.sheet_names)
except Exception as e:
    import traceback
    traceback.print_exc()
