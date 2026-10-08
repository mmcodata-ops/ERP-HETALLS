import re

file_path = 'frontend/src/pages/Dashboard.jsx'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  const currentIndex = data.findIndex(d => d.month === label)
  const previousDataRaw = currentIndex > 0 ? data[currentIndex - 1] : null
  const isCurrentPeriod = currentIndex === data.length - 1
  const previousData = (isCurrentPeriod && previousDataRaw && previousDataRaw.equiv) ? previousDataRaw.equiv : previousDataRaw"""

replacement = """  const currentIndex = data.findIndex(d => d.month === label)
  
  let previousDataRaw = null;
  if (chartGroupBy === 'day') {
    // Compare exactly 1 month prior (e.g. Oct 8 vs Sep 8)
    const currentDt = new Date(label);
    if (!isNaN(currentDt.getTime())) {
      const prevDt = new Date(currentDt);
      prevDt.setMonth(prevDt.getMonth() - 1);
      // Format to match label (e.g., "Sep 08, 2026")
      const prevLabel = prevDt.toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' });
      // Find that specific date in the dataset (if it was fetched, but note the API might only return last 30 days)
      // To fix this, we need the API to return the previous month's data too, or at least the equiv data.
      // Actually, if the API only returns the last 30 days, Sep 8 won't be in the dataset!
      previousDataRaw = data.find(d => d.month === prevLabel) || null;
    }
  } else {
    previousDataRaw = currentIndex > 0 ? data[currentIndex - 1] : null;
  }
  
  const isCurrentPeriod = currentIndex === data.length - 1
  const previousData = (isCurrentPeriod && previousDataRaw && previousDataRaw.equiv) ? previousDataRaw.equiv : previousDataRaw"""

# Wait! If the backend API only returns the last 30 days (sorted_months[-30:]), then `data` won't contain "Sep 08" when looking at "Oct 08"!
# We need to change the backend to either return more days, or supply the previous month's day inside the "equiv" object for the Daily view!
