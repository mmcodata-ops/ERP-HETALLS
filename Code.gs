/**
 * Google Apps Script - HTL International Sale Report (Zero-Latency Edition)
 */

const SHEET_ID = '1utksHJJpC3l37tBXMDoHrVy_ltSzW48O7rLeItXMQiY';
const SHEET_NAME = 'HTL- INTERNATIONAL SALE'; 
const ORDERS_SHEET_ID = '11NAw3BWNt3Bwcl1OqDv2EyL5WSLN1wZUg4qziq8SRDM';
const REMARK_SHEET_ID = '1lyKOWDulZxRHAtgp8P6kLvgsNbsDNm4CEP0TwvDGgcM';

const DISPLAY_COLUMNS = [
  { index: 1,  label: 'B'  },
  { index: 2,  label: 'C'  },
  { index: -1, label: 'ORDER_DATE' }, 
  { index: 4,  label: 'E'  },
  { index: 8,  label: 'I'  }, 
  { index: 10, label: 'K'  },
  { index: 11, label: 'L'  },
  { index: 13, label: 'N'  },
  { index: 17, label: 'R'  }, 
  { index: 21, label: 'V'  }, 
  { index: 52, label: 'BA' } 
];

const FILTER_COL_H = 7;
const DAYS_AGO_FILTER = 3; // Change to 0 if you want to show ALL unshipped orders
const MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

function doGet() {
  const template = HtmlService.createTemplateFromFile('form');
  
  try {
    template.preloadedData = getFilteredData();
  } catch(e) {
    template.preloadedData = JSON.stringify({ headers: [], rows: [], error: e.message });
  }

  return template.evaluate()
    .setTitle('HTL - International Sale Report')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// Backend function to save STATUS dynamically to Sheet127
function updateRemark(rfNo, value) {
  try {
    const ss = SpreadsheetApp.openById(REMARK_SHEET_ID);
    const sheet = ss.getSheetByName('Sheet127');
    if (!sheet) throw new Error('Sheet127 not found');
    
    const today = new Date();
    const dateStr = "[" + String(today.getDate()).padStart(2, '0') + "-" + MONTHS[today.getMonth()] + "-" + today.getFullYear() + "] ";

    let finalValue = String(value || '').trim();

    // Daily Formatting: Automatically prepend today's date if they added new unformatted data
    if (finalValue && !finalValue.startsWith("[")) {
      finalValue = dateStr + finalValue;
    }

    var tf = sheet.getRange("A:A").createTextFinder(rfNo).matchEntireCell(true).findNext();
    if (tf) {
      // Exists, update Column B
      sheet.getRange(tf.getRow(), 2).setValue(finalValue);
    } else {
      // Does not exist, append a brand new row at the bottom
      sheet.appendRow([rfNo, finalValue]);
    }
    
    // Return formatted value so the UI can update itself
    return finalValue;
  } catch (e) {
    throw new Error(e.message);
  }
}

function getFilteredData() {
  try {
    // 1. Fetch Ref# ID -> Order Date mapping from ORDERS sheet
    const orderDateMap = new Map();
    try {
      const ordersSs = SpreadsheetApp.openById(ORDERS_SHEET_ID);
      const ordersSheet = ordersSs.getSheetByName('ORDERS');
      if (ordersSheet) {
        const lastOrdersRow = ordersSheet.getLastRow();
        const maxOrdersCols = ordersSheet.getMaxColumns();
        if (lastOrdersRow > 1 && maxOrdersCols >= 4) {
          const fetchCols = Math.min(6, maxOrdersCols - 3); 
          const ordersData = ordersSheet.getRange(2, 4, lastOrdersRow - 1, fetchCols).getValues();
          for (var r = 0; r < ordersData.length; r++) {
            var refId = String(ordersData[r][0] || '').trim(); 
            if (refId) {
              orderDateMap.set(refId, fetchCols >= 6 ? ordersData[r][5] : ''); 
            }
          }
        }
      }
    } catch (e) {
      console.error("ORDERS fetch error: " + e.message);
    }

    // 2a. Fetch REMARK from ORDER REPORTS(Abhishek) (Ref No in Col A -> Remark in Col M)
    const abhishekRemarkMap = new Map();
    try {
      const abhiSs = SpreadsheetApp.openById(REMARK_SHEET_ID);
      const abhiSheet = abhiSs.getSheetByName('ORDER REPORTS(Abhishek)');
      if (abhiSheet) {
        const lastAbhiRow = abhiSheet.getLastRow();
        const maxAbhiCols = abhiSheet.getMaxColumns();
        
        if (lastAbhiRow > 1 && maxAbhiCols >= 13) {
          const abhiData = abhiSheet.getRange(2, 1, lastAbhiRow - 1, maxAbhiCols).getValues();
          for (var r = 0; r < abhiData.length; r++) {
            var rId = String(abhiData[r][0] || '').trim();
            if (rId) {
              var rawValue = abhiData[r][12];
              var displayValue = "";
              
              if (rawValue instanceof Date) {
                displayValue = String(rawValue.getDate()).padStart(2, '0') + '-' + MONTHS[rawValue.getMonth()] + '-' + rawValue.getFullYear();
              } else {
                displayValue = String(rawValue || '').trim();
              }
              abhishekRemarkMap.set(rId, displayValue);
            }
          }
        }
      }
    } catch (e) {
      console.error("Abhishek Remark fetch error: " + e.message);
    }

    // 2b. Fetch STATUS from Sheet127 (Ref No in Col A -> Status in Col B)
    const statusMap = new Map();
    try {
      const statusSs = SpreadsheetApp.openById(REMARK_SHEET_ID);
      const statusSheet = statusSs.getSheetByName('Sheet127');
      if (statusSheet) {
        const lastStatusRow = statusSheet.getLastRow();
        const maxStatusCols = statusSheet.getMaxColumns();
        if (lastStatusRow > 1 && maxStatusCols >= 2) {
          const statusData = statusSheet.getRange(2, 1, lastStatusRow - 1, maxStatusCols).getValues();
          for (var r = 0; r < statusData.length; r++) {
            var rId = String(statusData[r][0] || '').trim();
            if (rId) {
              var rawValue = statusData[r][1];
              var displayValue = "";
              
              if (rawValue instanceof Date) {
                displayValue = String(rawValue.getDate()).padStart(2, '0') + '-' + MONTHS[rawValue.getMonth()] + '-' + rawValue.getFullYear();
              } else {
                displayValue = String(rawValue || '').trim();
              }
              statusMap.set(rId, displayValue);
            }
          }
        }
      }
    } catch (e) {
      console.error("Sheet127 fetch error: " + e.message);
    }

    const ss = SpreadsheetApp.openById(SHEET_ID);

    // 3. Fetch Main Data
    const sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) throw new Error('Sheet "' + SHEET_NAME + '" not found.');

    const lastRow = sheet.getLastRow();
    if (lastRow < 3) return JSON.stringify({ headers: [], rows: [], error: 'No data found.' });
    
    const maxCols = sheet.getMaxColumns();
    const fetchCols = Math.min(53, maxCols);
    const allData = sheet.getRange(1, 1, lastRow, fetchCols).getValues();

    const headerRow = allData[1] || [];
    const headers = [];
    
    // Build Headers
    for (var j = 0; j < DISPLAY_COLUMNS.length; j++) {
      var col = DISPLAY_COLUMNS[j];
      
      if (col.label === 'ORDER_DATE') {
        headers.push('ORDER DATE');
        continue;
      }
      
      headers.push(String(headerRow[col.index] || ('Column ' + col.label)));
      if (col.label === 'I') headers.push('DAYS');
      if (col.label === 'BA') headers.push('STAR');
    }
    
    // Add REMARK (read-only from ORDER REPORTS(Abhishek))
    headers.push('REMARK');
    
    // Add STATUS (editable from Sheet127)
    headers.push('STATUS');

    const filteredRows = [];
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const todayTime = today.getTime();
    const msPerDay = 1000 * 3600 * 24;
    
    for (var i = 2; i < allData.length; i++) {
      var row = allData[i];
      var mainRefId = String(row[1] || '').trim();
      var colHValue = row[FILTER_COL_H];

      if (!colHValue || (typeof colHValue === 'string' && colHValue.trim() === '')) {
        var rawDate = row[8]; 
        var diffDays = 0;
        
        var sDate = null;
        if (rawDate instanceof Date) {
          sDate = new Date(rawDate.getTime());
        } else if (rawDate) {
          var parsed = new Date(rawDate);
          if (!isNaN(parsed.getTime())) {
            sDate = parsed;
          }
        }
        
        if (sDate) {
          sDate.setHours(0, 0, 0, 0);
          diffDays = Math.round((todayTime - sDate.getTime()) / msPerDay);
          if (diffDays < DAYS_AGO_FILTER) continue; 
        } else {
          continue; 
        }
        
        var displayRow = [];
        var isBlank = true;
        
        for (var j = 0; j < DISPLAY_COLUMNS.length; j++) {
          var col = DISPLAY_COLUMNS[j];
          var val;
          
          if (col.label === 'ORDER_DATE') {
            val = orderDateMap.get(mainRefId);
          } else {
            val = row[col.index];
          }
          
          if (val instanceof Date) {
            val = String(val.getDate()).padStart(2, '0') + '-' + MONTHS[val.getMonth()] + '-' + val.getFullYear();
          } else if (col.label === 'V' && typeof val === 'number') {
            val = val.toFixed(2);
          } else {
            val = (val !== null && val !== undefined) ? String(val).trim() : '';
          }
          
          if (val !== '') isBlank = false;
          displayRow.push(val);
          
          if (col.label === 'I') displayRow.push(diffDays); 
          if (col.label === 'BA') {
            var starStr = '';
            if (diffDays >= 7) starStr = '★★★';
            else if (diffDays >= 5) starStr = '★★';
            else if (diffDays >= 3) starStr = '★';
            displayRow.push(starStr);
          }
        }
        
        if (isBlank) continue;

        var abhishekRemark = abhishekRemarkMap.has(mainRefId) ? abhishekRemarkMap.get(mainRefId) : '';
        displayRow.push(abhishekRemark);

        var displayStatus = statusMap.has(mainRefId) ? statusMap.get(mainRefId) : '';
        displayRow.push(displayStatus);
        
        displayRow.push(diffDays); 
        filteredRows.push(displayRow);
      }
    }

    // Sort by diffDays (descending)
    filteredRows.sort(function(a, b) {
      return b[b.length - 1] - a[a.length - 1]; 
    });

    // Remove the hidden sorting column
    for (var r = 0; r < filteredRows.length; r++) {
      filteredRows[r].pop();
    }

    return JSON.stringify({
      headers: headers,
      rows: filteredRows
    });

  } catch (e) {
    return JSON.stringify({ headers: [], rows: [], error: e.message });
  }
}
