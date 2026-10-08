import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix table wrapper clipping
old_css = """  .breakdown-table-wrapper {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(40px) saturate(200%) !important;
    -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
    border-radius: 24px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-top: 1px solid rgba(255, 255, 255, 0.35) !important;
    border-left: 1px solid rgba(255, 255, 255, 0.25) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.15), inset 0 1px 2px rgba(255, 255, 255, 0.3) !important;
  
    gap: 14px;
    z-index: 9999;
    max-width: calc(100vw - 48px);
    max-height: calc(100vh - 90px);
    overflow: auto;
  
    margin: 0 24px 24px;
    flex: 1;
    min-height: 0;
    
  }"""

new_css = """  .breakdown-table-wrapper {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(40px) saturate(200%) !important;
    -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
    border-radius: 24px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-top: 1px solid rgba(255, 255, 255, 0.35) !important;
    border-left: 1px solid rgba(255, 255, 255, 0.25) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.15), inset 0 1px 2px rgba(255, 255, 255, 0.3) !important;
  
    gap: 14px;
    z-index: 9999;
    max-width: calc(100vw - 48px);
    overflow: auto;
  
    margin: 0 24px 24px;
    flex: 1;
    min-height: 0;
    
  }"""

if old_css in css:
    css = css.replace(old_css, new_css)
else:
    # use regex
    wrapper_regex = r"max-height:\s*calc\(100vh - 90px\);"
    css = re.sub(wrapper_regex, "", css)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed max-height clipping on table wrapper")
