import ezsheets

ss = ezsheets.Spreadsheet('1C70rvR0hIeHCUHcAVSAmyd_pv-twWf3bNSyPDON3Ixg')
print(ss.title) # The title of the spreadsheet.
ss.title = 'Example Spreadsheet' # Change the title of the spreadsheet.
print(ss.spreadsheetId) # The ID of the spreadsheet.
print(ss.url) # The URL of the spreadsheet.
print(ss.sheetTitles) # The titles of all the sheets in the spreadsheet.
print(ss.sheets) # The Sheet objects in the spreadsheet.
print(ss[0]) # The first sheet in the spreadsheet.
print(ss['Data']) # The first sheet in the spreadsheet.
#del ss[1] # Delete the second sheet in the spreadsheet.
print(ss.sheetTitles) # The titles of all the sheets in the spreadsheet.
#ss.downloadAsExcel() # Download the spreadsheet as an Excel file.

sheet = ss[0] # Get the first sheet in the spreadsheet.
print(sheet.title) # The title of the sheet.

ss.createSheet('Sales') # Create a new sheet in the spreadsheet.
sheet = ss[1] # Get the new sheet.
sheet['A1'] = 'Name' # Write 'Name' to cell A1.
sheet['B1'] = 'Age' # Write 'Age' to cell B1.
print(sheet['A1']) # The value in cell A1.
print(sheet['A2']) # The value in cell A2.
print(sheet[2, 1]) # Column 2, Row 1 is the same address as B1.
sheet['A2'] = 'Alice' # Write 'Alice' to cell A2.
sheet['B2'] = 30 # Write 30 to cell B2.
sheet['C2'] = 'RoboCop' # Write 'RoboCop' to cell C2.
sheet.refresh() # Refresh the sheet to see the changes.


