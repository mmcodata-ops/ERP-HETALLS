import re

file_path = 'frontend/src/index.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

target = """.glass-switch[data-v="ho"] .glass-switch-knob, .glass-switch[data-v="week"] .glass-switch-knob { transform: translateX(100%); }"""
replacement = """.glass-switch[data-v="ho"] .glass-switch-knob, .glass-switch[data-v="week"] .glass-switch-knob, .glass-switch[data-v="day"] .glass-switch-knob { transform: translateX(100%); }"""

css = css.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("index.css patched")
