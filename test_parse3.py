from datetime import datetime
date_str = '25/08/2026'
formats = [
    "%d-%b-%Y", "%d-%b-%y", "%d %b %Y", "%d %b %y",
    "%b %d, %Y", "%b %d %Y", "%d-%B-%Y", "%d %B %Y",
    "%B %d, %Y", "%B %d %Y", "%d/%m/%Y", "%m/%d/%Y",
    "%d/%m/%y", "%m/%d/%y", "%d-%m-%Y", "%m-%d-%Y",
    "%d-%m-%y", "%m-%d-%y", "%Y-%m-%d", "%Y/%m/%d"
]
for fmt in formats:
    try:
        dt = datetime.strptime(date_str, fmt)
        print(f"Success with {fmt}: {dt}")
        break
    except ValueError:
        pass
