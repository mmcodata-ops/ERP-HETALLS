import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

pattern = r"body\s*\{[^\}]*?min-height:\s*100vh;[^\}]*\}"
new_body = """body {
  font-family: 'Inter', sans-serif;
  background-color: #050811;
  background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  position: relative;
  z-index: 0;
}
body::before {
  content: '';
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(5, 8, 17, 0.4);
  z-index: -1;
}"""

css, count = re.subn(pattern, new_body, css, flags=re.DOTALL)
if count > 0:
    with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Body background updated successfully.")
else:
    print("Could not match body block.")
