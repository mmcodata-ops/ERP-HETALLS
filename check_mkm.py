import pandas as pd
import sys
url = "https://docs.google.com/spreadsheets/d/1NZo52WV0ynaYe-G2WrZ5ItRwPmNKjdwhr_GOyztAz8U/export?format=xlsx"
try:
    xl = pd.ExcelFile(url)
    for sheet in xl.sheet_names:
        df = pd.read_excel(url, sheet_name=sheet)
        mask = df.astype(str).apply(lambda x: x.str.contains('Alyson', case=False, na=False)).any(axis=1)
        if not df[mask].empty:
            print(f"FOUND ALYSON IN MKM: tab = {sheet}")
            sys.exit(0)
    print("Not found in MKM")
except Exception as e:
    print(e)
