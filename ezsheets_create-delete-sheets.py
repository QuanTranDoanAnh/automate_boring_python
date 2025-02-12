import ezsheets

ss = ezsheets.createSpreadsheet('Multiple Sheets')
print(ss.sheetTitles)

sheet = ss.createSheet('Spam') # Create a new sheet at the end of the list of sheets.
print(sheet)

ss.createSheet('Eggs') # Create another new sheet.
print(ss.sheetTitles)

sheet2 = ss.createSheet('Bacon', 0) # Create a new sheet at the start of the list of sheets.
print(ss.sheetTitles)