#!/usr/bin/python2
from pyPdf import PdfFileReader
import os

pdfDictionary = {}

choice = 'unset'
while choice not in set(['y','n']):
    choice = raw_input("Do you want to look into subfolders? [y,n] ").lower()

lookAtSubFolders = False
if choice == 'y': lookAtSubFolders = True

nPDFFiles=0
if lookAtSubFolders:
    for root, dirs, files in os.walk("./"):
	for file in files:
            if file.endswith(".pdf"):
		nPDFFiles+=1
		filePath=os.path.join(root, file)
		filePdf=PdfFileReader(open(filePath,'rb'))
		pdfDictionary[filePath]=filePdf.getNumPages()
else:
    for file in os.listdir("./"):
	if file.endswith(".pdf"):
	    nPDFFiles+=1
	    filePdf=PdfFileReader(open(file,'rb'))
	    pdfDictionary[file]=filePdf.getNumPages()

print
totPag = 0
for entry in pdfDictionary:
    print entry, pdfDictionary[entry]
    totPag+=pdfDictionary[entry]

print
print "Number of PDFs:", nPDFFiles
print "Total pages:", totPag
