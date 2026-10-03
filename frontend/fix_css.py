import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Body
css = re.sub(
    r'body \{[^}]*min-height: 100vh;[^}]*\}',
    '''body {
  font-family: 'Inter', sans-serif;
  background-color: #030812;
  background-image: 
    radial-gradient(circle at 10% 20%, rgba(14, 165, 233, 0.15) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 40%),
    radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.1) 0%, transparent 60%);
  background-attachment: fixed;
  color: var(--text-primary);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}''',
    css, flags=re.DOTALL
)

# 2. Update .card
css = re.sub(
    r'\.card \{.*?box-shadow:.*?;.*?\}',
    '''.card {
  background: rgba(20, 30, 45, 0.25) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 32px;
  padding: 24px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
}''',
    css, flags=re.DOTALL
)

# 3. Update .kpi-card
css = re.sub(
    r'\.kpi-card \{.*?box-shadow:.*?;.*?\}',
    '''.kpi-card {
  background: rgba(20, 30, 45, 0.25);
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 32px;
  padding: 20px;
  transition: all var(--transition);
  position: relative; overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
}''',
    css, flags=re.DOTALL
)

# 4. Update .login-card
css = re.sub(
    r'\.login-card \{.*?z-index: 1;.*?\}',
    '''.login-card {
  background: rgba(20, 30, 45, 0.25);
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 32px;
  padding: 48px 44px;
  width: 420px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
  position: relative; z-index: 1;
}''',
    css, flags=re.DOTALL
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Done styling')
