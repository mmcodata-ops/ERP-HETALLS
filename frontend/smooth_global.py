import sys

def replace_in_file(filepath, old_str, new_str):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace(old_str, new_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)

# Replace in index.css
replace_in_file(
    'frontend/src/index.css',
    "--vision-spring: cubic-bezier(0.34, 1.4, 0.64, 1);",
    "--vision-spring: cubic-bezier(0.22, 1, 0.36, 1);"
)

replace_in_file(
    'frontend/src/index.css',
    "transform: translateX(-110%) !important;\n    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;",
    "transform: translateX(-110%) !important;\n    transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1) !important;"
)

print("Smoothed out global animations.")
