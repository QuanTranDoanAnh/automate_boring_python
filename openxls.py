import openpyxl

wb = openpyxl.load_workbook('data/example.xlsx')
print(wb.sheetnames)
sheet = wb['Data']
print(sheet.title)
print(type(sheet))
anotherSheet = wb.active
print(anotherSheet.title)