import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Completely rebuild the mobile media query for the sidebar to ensure it hides and functions correctly
mobile_fixes_pattern = r'/\* --- SIDEBAR MOBILE FIXES --- \*/[\s\S]*?(?=\n/\*|$)'
new_mobile_fixes = """/* --- SIDEBAR MOBILE FIXES --- */
@media (max-width: 900px) {
  .sidebar {
    background: rgba(10, 12, 20, 0.95) !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    border-radius: 0 !important;
    border: none !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
    box-shadow: 20px 0 60px rgba(0, 0, 0, 0.5) !important;
    
    position: fixed !important;
    top: 0 !important; 
    left: 0 !important;
    height: 100vh !important;
    width: 280px !important;
    
    transform: translateX(-110%) !important;
    transition: transform 0.4s ease-out !important;
    z-index: 9999 !important;
  }
  
  .sidebar.mobile-open {
    transform: translateX(0) !important;
  }

  .mobile-close-btn {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--text-muted);
    width: 32px;
    height: 32px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10000;
  }
  
  .mobile-backdrop {
    display: block;
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    z-index: 9998;
    animation: fadeIn 0.3s ease;
  }
  
  .mobile-menu-btn {
    margin-right: 12px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 8px;
    color: white;
    cursor: pointer;
    display: flex;
  }
}"""

if '/* --- SIDEBAR MOBILE FIXES --- */' in css:
    css = re.sub(mobile_fixes_pattern, new_mobile_fixes, css)
else:
    # Append it to the end if not found
    css += "\n\n" + new_mobile_fixes

# Also remove the duplicate broken sidebar declaration from inside @media (max-width: 900px) that was accidentally created
broken_sidebar_in_media = r'@media \(max-width: 900px\) \{[\s\S]*?\.sidebar\s*\{[^}]*z-index: 100;\s*overflow-y: auto;\s*\}'
# We will just replace it by doing a more targeted clean up
css = re.sub(r'  \.sidebar \{\s*background: var\(--vision-glass\) !important;[\s\S]*?overflow-y: auto;\s*\}', '', css)


with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed mobile sidebar layout.")
