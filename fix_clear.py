import re

with open('frontend/src/pages/Dashboard.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing clearInterval
bad_block = '''      }, 5000); // Poll every 5 seconds
    }
  }, [showBreakdown, bdTab, bdCustomDate, bdCustomEndDate, API])'''

good_block = '''      }, 5000); // Poll every 5 seconds
    }
    return () => clearInterval(interval);
  }, [showBreakdown, bdTab, bdCustomDate, bdCustomEndDate, API])'''

if bad_block in content:
    content = content.replace(bad_block, good_block)
    with open('frontend/src/pages/Dashboard.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed clearInterval!")
else:
    print("Could not find block to replace.")
