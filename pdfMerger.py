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

print 'Writing output...'
merger.write("output.pdf")
