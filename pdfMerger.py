#!/usr/bin/python2
from PyPDF2 import PdfFileReader, PdfFileMerger
import os

print 'Loading documents...'
merger = PdfFileMerger()
pdfFiles = []
for filename in os.listdir("./"):
    if filename.endswith(".pdf"):
	pdfFiles.append(filename)

print 'Sorting documents...'
pdfFiles.sort()

print 'Merging...'
for pdfFile in pdfFiles:
    merger.append(PdfFileReader(file(pdfFile, 'rb')))

fileName = raw_input("Insert output file name: [default output.pdf] ")
if fileName == '':
    fileName='output.pdf'
    
print 'Writing output...'
merger.write(fileName)
