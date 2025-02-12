import re
import os
import shutil

download_dir = r'C:\Downloads'
OCEAN_PDF_PREFIX = r'^_OceanofPDF.com_'
UNDERSCORE_CHAR = r'_'
SPACE_CHAR = r' '
BLANK_CHAR = r''

filenamePattern = re.compile(OCEAN_PDF_PREFIX)
# Loop over all the Ocean PDF files
for oceanPDFfilename in os.listdir(download_dir):
    mo = filenamePattern.search(oceanPDFfilename)
    
    # Skip files out of the scope
    if mo == None:
        continue
    else:
        newOceanPdfFilename = re.sub(OCEAN_PDF_PREFIX, BLANK_CHAR, oceanPDFfilename)
        newOceanPdfFilename = re.sub(UNDERSCORE_CHAR, SPACE_CHAR, newOceanPdfFilename)
        print(newOceanPdfFilename) 
        
        absWorkingPath = os.path.abspath(download_dir)
        oceanPDFfilename = os.path.join(absWorkingPath, oceanPDFfilename)
        newOceanPdfFilename = os.path.join(absWorkingPath, newOceanPdfFilename)
        print(f'Renaming "{oceanPDFfilename}" to "{newOceanPdfFilename}"...')
        shutil.move(oceanPDFfilename, newOceanPdfFilename)
