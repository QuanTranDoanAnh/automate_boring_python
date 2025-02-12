import ezsheets

ss = ezsheets.Spreadsheet('1C70rvR0hIeHCUHcAVSAmyd_pv-twWf3bNSyPDON3Ixg')
sheet = ss[0]
print(ezsheets.convertAddress('A2')) # Convert addresses
print(ezsheets.convertAddress(1, 2)) # ...and converts them back, too.
print(ezsheets.getColumnLetterOf(2))  # Convert column number to letter
print(ezsheets.getColumnNumberOf('B')) # Convert column letter to number
print(ezsheets.getColumnLetterOf(999)) # Convert column number to letter
print(ezsheets.getColumnNumberOf('ZZZ')) # Convert column letter to number

