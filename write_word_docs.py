#! python3
import docx

doc = docx.Document()
doc.add_paragraph('Hello world!')
doc.save('./data/helloworld.docx')