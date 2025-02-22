import PyPDF2
pdfFileReader = PyPDF2.PdfReader(open('./data/encrypted.pdf', 'rb'))
print(pdfFileReader.is_encrypted)
#pageObj = pdfFileReader.pages[0]
#print(pageObj)
pdfFileReader.decrypt('rosebud')
pageObj = pdfFileReader.pages[0]
print(pageObj)