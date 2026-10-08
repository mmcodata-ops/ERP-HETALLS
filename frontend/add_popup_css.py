import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Card Hover Details Popup */
.card-detail-popup {
  position: absolute;
  top: 105%;
  left: 50%;
  transform: translateX(-50%);
  min-width: 260px;
  z-index: 9999;
  background: #070b16;
  border: 1px solid var(--border-accent);
  border-radius: 12px;
  padding: 14px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), var(--glass-shine);
}

@media (max-width: 900px) {
  /* On mobile, move the detail popup to the top part of the screen so it doesn't get cut off on edges */
  .card-detail-popup {
    position: fixed !important;
    top: 100px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 90vw !important;
    max-width: 320px !important;
    max-height: 70vh !important;
    overflow-y: auto !important;
  }
  
  /* Make Recharts tooltips fixed on mobile so they don't cover the bars when clicked */
  .recharts-tooltip-wrapper {
    position: fixed !important;
    top: 80px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    transition: none !important;
    z-index: 10000 !important;
    width: max-content;
  }
}
"""

if '.card-detail-popup' not in css:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css + new_css)
    print("index.css updated with popup styles")
else:
    print("Already updated")
