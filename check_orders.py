import pandas as pd
url = "https://docs.google.com/spreadsheets/d/1vTkTIObrXy88vQVg2_bAI2T8vPa1tXT5IWZw8tdvF9BW7aYj9qqTA6WeZjpJHlBlw4dpTj_o7dYhtzW/export?format=xlsx"
try:
    xl = pd.ExcelFile(url)
    print("Sheets in ORDERS:", xl.sheet_names)
except Exception as e:
    import traceback
    traceback.print_exc()
