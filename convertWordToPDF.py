#! python3
"""
The PyPDF2 module doesn’t allow you to create PDF documents directly, but there’s a way to generate PDF files with Python 
if you’re on Windows and have Microsoft Word installed. You’ll need to install the Pywin32 package by 
running `pip install --user -U pywin32==308`. 
With this and the docx module, you can create Word documents and then convert them to PDFs with the following script.
"""
import win32com.client # install with "pip install pywin32==308"
import docx

wordFilename = 'your_word_document.docx'
pdfFilename = 'your_pdf_filename.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)

wdFormatPDF = 17 # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()