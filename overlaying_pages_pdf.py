import PyPDF2

minutesFile = open('./data/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
minutesFirstPage = pdfReader.pages[0]
pdfWatermarkReader = PyPDF2.PdfReader(open('./data/watermark.pdf', 'rb'))
minutesFirstPage.merge_page(pdfWatermarkReader.pages[0])
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(minutesFirstPage)

for pageNum in range(1, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)
    
resultPdfFile = open('./data/watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
