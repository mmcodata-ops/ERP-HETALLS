import re

with open('backend/routers/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Change time.sleep(15) to time.sleep(120) for the background thread
content = re.sub(r'time\.sleep\(15\)\s*# Refresh exactly every 15 seconds!', 'time.sleep(60) # Refresh every 60 seconds to avoid Google Rate Limits', content)

# Change timeout=30 to timeout=10 in requests.get
content = content.replace('timeout=30', 'timeout=10')

# Change event.wait() without timeout to event.wait(timeout=10)
content = re.sub(r'event\.wait\(\)', 'event.wait(timeout=10)', content)
content = re.sub(r'event\.wait\(timeout=20\)', 'event.wait(timeout=10)', content)

with open('backend/routers/dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
