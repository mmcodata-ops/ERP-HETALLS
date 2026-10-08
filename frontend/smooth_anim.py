import sys

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace(old_str, new_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)

# Replace in Dashboard.jsx
replace_in_file(
    'frontend/src/pages/Dashboard.jsx',
    "transition: 'transform 0.4s cubic-bezier(0.34, 1.4, 0.64, 1)'",
    "transition: 'transform 0.45s cubic-bezier(0.22, 1, 0.36, 1)'"
)

# Replace in Sidebar.jsx
replace_in_file(
    'frontend/src/components/Sidebar.jsx',
    'transition: "all 0.4s cubic-bezier(0.34, 1.4, 0.64, 1)"',
    'transition: "all 0.45s cubic-bezier(0.22, 1, 0.36, 1)"'
)

print("Smoothed out animations.")
