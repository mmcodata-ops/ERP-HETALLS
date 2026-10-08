import sys
import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add background colorful blobs for the visionOS effect
bg_css = """
:root {
  --vision-bg: #000000;
  --vision-glass: rgba(255, 255, 255, 0.03);
  --vision-glass-hover: rgba(255, 255, 255, 0.08);
  --vision-border: rgba(255, 255, 255, 0.08);
  --vision-border-light: rgba(255, 255, 255, 0.25);
  --vision-shadow: 0 24px 60px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.2);
  --vision-spring: cubic-bezier(0.34, 1.4, 0.64, 1);
}

body {
  background-color: var(--vision-bg) !important;
  background-image: 
    radial-gradient(circle at 15% 50%, rgba(147, 51, 234, 0.15), transparent 40%),
    radial-gradient(circle at 85% 30%, rgba(59, 130, 246, 0.15), transparent 40%),
    radial-gradient(circle at 50% 80%, rgba(212, 175, 55, 0.1), transparent 40%) !important;
  background-attachment: fixed;
}
"""

if ":root {" in css:
    css = css.replace(":root {", bg_css + "\n:root {", 1)

# 2. Update all main containers to use the exact visionOS glass rules requested
glass_pattern = r"background:\s*rgba\([^)]+\)\s*!important;\s*backdrop-filter:[^;]+;\s*(?:-webkit-backdrop-filter:[^;]+;\s*)?border-radius:[^;]+;\s*border:[^;]+;\s*(?:border-[^;]+;\s*)*box-shadow:[^;]+;"

visionos_glass = """background: var(--vision-glass) !important;
  backdrop-filter: blur(40px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
  border: 1px solid var(--vision-border) !important;
  border-top: 1px solid var(--vision-border-light) !important;
  border-left: 1px solid var(--vision-border-light) !important;
  box-shadow: var(--vision-shadow) !important;"""

# Replace in .sidebar, .header, .kpi-card, .table-wrapper
css = re.sub(r"\.sidebar\s*\{[^}]*background:[^}]*\}", lambda m: re.sub(glass_pattern, visionos_glass, m.group(0)), css)
css = re.sub(r"\.header\s*\{[^}]*background:[^}]*\}", lambda m: re.sub(glass_pattern, visionos_glass, m.group(0)), css)
css = re.sub(r"\.kpi-card\s*\{[^}]*background:[^}]*\}", lambda m: re.sub(glass_pattern, visionos_glass, m.group(0)), css)
css = re.sub(r"\.table-wrapper.*?\s*\{[^}]*background:[^}]*\}", lambda m: re.sub(glass_pattern, visionos_glass, m.group(0)), css)

# 3. Update Hover states and spring animations
css = css.replace("transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);", "transition: all 0.4s var(--vision-spring);")
css = css.replace("transition: all 0.3s ease;", "transition: all 0.4s var(--vision-spring);")

# Enhance KPI card hover
kpi_hover = r"\.kpi-card:hover\s*\{[^}]+\}"
new_kpi_hover = """.kpi-card:hover {
  background: var(--vision-glass-hover) !important;
  transform: translateY(-2px);
  box-shadow: 0 32px 72px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.3) !important;
}"""
css = re.sub(kpi_hover, new_kpi_hover, css)

# 4. KPI Grid Responsive requirements (6-card: 3x2 on tablet, 2x3 on mobile)
# The user wants exact breakpoints
responsive_block = """
/* --- VISIONOS KPI GRID --- */
.kpi-grid {
  display: grid !important;
  grid-template-columns: repeat(6, 1fr) !important;
  align-items: stretch !important;
}
.kpi-grid > * {
  flex: 1 !important;
}
@media (max-width: 1100px) {
  .kpi-grid { grid-template-columns: repeat(3, 1fr) !important; }
}
@media (max-width: 768px) {
  .kpi-grid { grid-template-columns: repeat(2, 1fr) !important; }
}
@media (max-width: 480px) {
  .kpi-grid { grid-template-columns: 1fr !important; } /* Fallback for very small */
}
"""
css = re.sub(r"/\* --- MOBILE RESPONSIVENESS OVERRIDES --- \*/.*", responsive_block, css, flags=re.DOTALL)

with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied VisionOS CSS.")
