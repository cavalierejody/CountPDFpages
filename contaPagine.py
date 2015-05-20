#!/usr/bin/python2
from pyPdf import PdfFileReader
import os

"""""
for file in os.listdir("./"):
    if file.endswith(".pdf"):
        print(file)
"""""

pdfDictionary = {}

choice = 'unset'
while choice not in set(['y','n']):
    choice = raw_input("Do you want to look into subfolders? [y,n] ").lower()

lookAtSubFolders = False
if choice == 'y': lookAtSubFolders = True

if lookAtSubFolders:
    for root, dirs, files in os.walk("./"):
	for file in files:
            if file.endswith(".pdf"):
		filePath=os.path.join(root, file)
		filePdf=PdfFileReader(open(filePath,'rb'))
		pdfDictionary[filePath]=filePdf.getNumPages()
else:
    for file in os.listdir("./"):
	if file.endswith(".pdf"):
		filePdf=PdfFileReader(open(file,'rb'))
		pdfDictionary[file]=filePdf.getNumPages()

print
totPag = 0
for entry in pdfDictionary:
    print entry, pdfDictionary[entry]
    totPag+=pdfDictionary[entry]

print
print "Total pages:", totPag
