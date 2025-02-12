import ezsheets

# spreadsheet = ezsheets.Spreadsheet('1KzQyNS8XvheXIN4nUVOfWhMmcYBIBSubr8oRHOIaJHc')
# print(spreadsheet.title)

# spreadsheet2 = ezsheets.createSpreadsheet('My new Spreadsheet')
# print(spreadsheet2.title)

spreadsheet3 = ezsheets.upload('./data/example.xlsx')
print(spreadsheet3.title)

# print(ezsheets.listSpreadsheets())