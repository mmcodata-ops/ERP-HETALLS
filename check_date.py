from datetime import datetime

formats = [
    "%d-%b-%Y", "%d-%b-%y", "%d %b %Y", "%d %b %y",
    "%b %d, %Y", "%b %d %Y", "%d-%B-%Y", "%d %B %Y",
    "%B %d, %Y", "%B %d %Y", "%d/%m/%Y", "%m/%d/%Y",
    "%d/%m/%y", "%m/%d/%y", "%d-%m-%Y", "%m-%d-%Y",
    "%d-%m-%y", "%m-%d-%y", "%Y-%m-%d", "%Y/%m/%d"
]
date_str = "4-April-26"
success = False
for fmt in formats:
    try:
        dt = datetime.strptime(date_str, fmt)
        print(f"Success with {fmt}: {dt}")
        success = True
        break
    except ValueError:
        pass
if not success:
    print("FAILED to parse '4-April-26'")
