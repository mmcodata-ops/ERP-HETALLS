import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a comprehensive mobile override block at the end of the CSS
mobile_sidebar_override = """
/* --- SIDEBAR MOBILE FIXES --- */
@media (max-width: 900px) {
  .sidebar {
    background: rgba(14, 16, 25, 0.95) !important; /* Make it solid dark so it's readable over the dashboard */
    backdrop-filter: blur(20px) saturate(150%) !important;
    -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
    border-radius: 0 24px 24px 0 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-left: none !important;
    
    top: 0 !important; 
    left: 0 !important;
    height: 100vh !important;
    width: 280px !important;
    
    transform: translateX(-110%);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    z-index: 9999 !important;
  }
  
  .sidebar.mobile-open {
    transform: translateX(0) !important;
    box-shadow: 20px 0 60px rgba(0, 0, 0, 0.8) !important;
  }

  .mobile-close-btn {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(255, 255, 255, 0.1);
    border: none;
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10000;
  }
  
  .sidebar-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    z-index: 9998;
    animation: fadeIn 0.3s ease;
  }
  
  /* Ensure header hamburger menu doesn't overlap text awkwardly */
  .mobile-menu-btn {
    margin-right: 12px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    padding: 8px;
    color: white;
    cursor: pointer;
  }
}
"""

if "/* --- SIDEBAR MOBILE FIXES --- */" not in css:
    css += "\n" + mobile_sidebar_override
else:
    css = re.sub(r"/\* --- SIDEBAR MOBILE FIXES --- \*/.*", mobile_sidebar_override, css, flags=re.DOTALL)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added sidebar mobile fixes.")
