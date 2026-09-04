import pandas as pd

def search_alyson(url, name):
    try:
        xl = pd.ExcelFile(url)
        for sheet in xl.sheet_names:
            df = pd.read_excel(url, sheet_name=sheet)
            mask = df.astype(str).apply(lambda x: x.str.contains('Alyson', case=False, na=False)).any(axis=1)
            if not df[mask].empty:
                print(f"Found Alyson in {name} -> tab: {sheet}")
                print(df.columns)
                return True
        print(f"Not found in {name}")
    except Exception as e:
        print(e)

search_alyson("https://docs.google.com/spreadsheets/d/1NZo52WV0ynaYe-G2WrZ5ItRwPmNKjdwhr_GOyztAz8U/export?format=xlsx", "MKM")
search_alyson("https://docs.google.com/spreadsheets/d/11NAw3BWNt3Bwcl1OqDv2EyL5WSLN1wZUg4qziq8SRDM/export?format=xlsx", "CARPET")
