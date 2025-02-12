import ezsheets

ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
print(ss1[0])

ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
ss1[0].copyTo(ss2) # Copy the ss1's Sheet1 to the ss2 spreadsheet.
print(ss2[1].getRows())
print(ss2.sheetTitles)