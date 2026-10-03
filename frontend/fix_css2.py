import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.sidebar \{.*?box-shadow:.*?;.*?\}',
    '''.sidebar {
  position: fixed;
  top: 0; left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  background: rgba(10, 20, 35, 0.4) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 10px 0 35px rgba(0, 0, 0, 0.3) !important;
}''',
    css, flags=re.DOTALL
)

css = re.sub(
    r'\.header \{.*?z-index: 10;.*?\}',
    '''.header {
  height: var(--header-height);
  background: rgba(10, 20, 35, 0.3) !important;
  backdrop-filter: blur(28px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(180%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
  position: sticky; top: 0; z-index: 10;
}''',
    css, flags=re.DOTALL
)

# And let's make the breakdown table wrapper glass too
css = re.sub(
    r'\.breakdown-table-wrapper \{.*?min-height: 0;.*?\}',
    '''.breakdown-table-wrapper {
  overflow: auto;
  background: rgba(20, 30, 45, 0.25) !important;
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 20px;
  flex: 1;
  min-height: 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25), inset 0 1px 1px rgba(255,255,255,0.15);
}''',
    css, flags=re.DOTALL
)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Done styling extra elements')
