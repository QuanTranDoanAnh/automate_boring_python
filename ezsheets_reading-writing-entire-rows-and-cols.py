import ezsheets

ss = ezsheets.upload('./data/produceSales.xlsx')
sheet = ss[0]
print(sheet.getRow(1)) # The first row is row 1, not row 0.
print(sheet.getRow(2)) # The second row is row 2.
columnOne = sheet.getColumn(1)
print(columnOne)
print(sheet.getColumn('A')) # Same result as getColumn(1)
print(sheet.getRow(3))
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
print(sheet.getRow(3))
columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    # Make the Python list contain uppercase strings:
    columnOne[i] = value.upper()

# sheet.updateColumn(1, columnOne)  # Update the entire column in one go.
rows = sheet.getRows() # Get every row in the spreadsheet.
print(rows[0])
print(rows[1])
rows[1][0] = 'PUMPKIN' # Change the produce name.
print(rows[1])
print(rows[10])
rows[10][2] = '400' # Change the pounds sold.
rows[10][3] = '904' # Change the total.
print(rows[10])
sheet.updateRows(rows) # Update the online spreadsheet with the changes.
print(sheet.rowCount)
print(sheet.columnCount)
