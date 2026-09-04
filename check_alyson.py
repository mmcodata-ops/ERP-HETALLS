import pandas as pd
url = "https://docs.google.com/spreadsheets/d/11NAw3BWNt3Bwcl1OqDv2EyL5WSLN1wZUg4qziq8SRDM/export?format=xlsx"
try:
    df = pd.read_excel(url, sheet_name="ORDERS")
    mask = df.astype(str).apply(lambda x: x.str.contains('Alyson', case=False, na=False)).any(axis=1)
    if not df[mask].empty:
        print("Found Alyson in ORDERS tab of CARPET sheet!")
        print(df.columns)
    else:
        print("Not found in ORDERS tab.")
        
    df2 = pd.read_excel(url, sheet_name="CARPET")
    mask2 = df2.astype(str).apply(lambda x: x.str.contains('Alyson', case=False, na=False)).any(axis=1)
    if not df2[mask2].empty:
        print("Found Alyson in CARPET tab of CARPET sheet!")
        print(df2.columns)
    else:
        print("Not found in CARPET tab.")
except Exception as e:
    import traceback
    traceback.print_exc()
