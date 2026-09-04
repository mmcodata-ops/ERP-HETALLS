with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove the fetchAll interval (5 seconds)
content = content.replace('const interval = setInterval(() => fetchAll(false), 5000);', '')
content = content.replace('clearInterval(interval);', '')

# Second, fix the breakdown interval
# We will completely remove the useEffect for the breakdown interval!
# Wait, the useEffect might do other things? Let's check!
