#! python3
# csv_dictreader_dictwriter.py - Read CSV file with csv.DictReader() and write CSV file with csv.DictWriter()

import csv

exampleFile = open('./data/exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
    
# File with no header yet
exampleFile = open('./data/example.csv')
exampleDictReader = csv.DictReader(exampleFile, fieldnames=['time', 'name', 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

# DictWriter
outputFile = open('./data/output_dict.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'Cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-8080', 'Name': 'Carol', 'Pet': 'Bird'})
outputFile.close()
print('Done')