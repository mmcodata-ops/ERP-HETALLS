with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "Monthly Revenue Trend" in line:
            print("FOUND at line", i)
            for j in range(i-2, i+5):
                print(repr(lines[j]))
