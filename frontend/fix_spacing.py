import re

with open('frontend/src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .main-content desktop layout overflow
old_main_content = r"\.main-content\s*\{\s*flex: 1;\s*margin-left: calc\(var\(--sidebar-width\) \+ 24px\);\s*min-height: 100vh;\s*display: flex;\s*flex-direction: column;\s*\}"
new_main_content = """.main-content {
  margin-left: var(--sidebar-width);
  width: calc(100vw - var(--sidebar-width));
  max-width: calc(100vw - var(--sidebar-width));
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}"""

if re.search(old_main_content, css):
    css = re.sub(old_main_content, new_main_content, css)
else:
    # Try more generic match
    generic_match = r"\.main-content\s*\{[^}]*margin-left:[^}]*\}"
    def replace_main(m):
        return new_main_content
    css = re.sub(generic_match, replace_main, css, count=1)


# Also ensure mobile view gives a tiny bit of breathing room
# The mobile main-content override:
old_mobile_main = r"\.main-content\s*\{\s*margin-left: 0 !important;\s*width: 100% !important;\s*max-width: 100vw !important;\s*\}"
new_mobile_main = """.main-content {
    margin-left: 0 !important;
    width: 100vw !important;
    max-width: 100vw !important;
  }"""
css = re.sub(old_mobile_main, new_mobile_main, css)


with open('frontend/src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed main-content layout to prevent horizontal overflow and add space.")
