#! python3
# printTable.py - that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified

def printTable(tableData):
    # find largest column width of every columns
    colWidths = [0] * len(tableData)
    # find number of rows per column
    colRowCount = []
    for colIdx in range(len(tableData)):
        columnElementWidths = [len(element) for element in tableData[colIdx]]
        columnElementWidths.sort(reverse=True) # sort in descending order for element widths found above
        # largest width is the 1st element of the columnElementWidths
        colWidths[colIdx] = columnElementWidths[0]
        colRowCount.append(len(tableData[colIdx]))
    # print the table data    
    maxRowCount = sorted(colRowCount, reverse=True)[0]    
    for rowIdx in range(maxRowCount):
        row = ''
        for colIdx in range(len(tableData)):
            if len(tableData[colIdx]) > rowIdx:
                row += tableData[colIdx][rowIdx].rjust(colWidths[colIdx] + 1)
            else:
                row += ' '.rjust(colWidths[colIdx] + 1)
        print(row)

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David', 'Teddy', 'Chris'],
    ['dogs', 'cats', 'moose', 'goose', 'hummingbird']
]
printTable(tableData)