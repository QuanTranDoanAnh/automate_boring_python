#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2, os
# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('./data'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(os.path.join('.', 'data', filename), 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # Only processing non-encrypted files
    if not pdfReader.is_encrypted:
        # Loop through all the pages (except the first) and add them.
        for pageNum in range(1, len(pdfReader.pages)):
            pageObj = pdfReader.pages[pageNum]
            pdfWriter.add_page(pageObj)
# Save the resulting PDF to a file.
pdfOutput = open(os.path.join('.', 'data', 'allminutes.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()