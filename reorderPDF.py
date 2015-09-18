#!/usr/bin/python2

print
print "Programma per l'acquisizione fronte/retro tramite scanner"
print "                                   copyright Jody Cavalli"

import sys
import random

from pyPdf import PdfFileWriter, PdfFileReader

# read input pdf and instantiate output pdf
output = PdfFileWriter()
input1 = PdfFileReader(file(sys.argv[1],"rb"))

# construct and shuffle page number list
nPages = input1.getNumPages()
print "n. pagine: " , nPages

firstHalf = list(range(nPages/2))
secondHalf = list(range(nPages-1,nPages/2-1,-1))

pages = []

for i in range(nPages/2):
#    print i
    pages.append(firstHalf[i])
    pages.append(secondHalf[i])

# display new sequence
print "Riordinamento delle pagine secondo la successione:"
print pages

# add  the new sequence of pages to output pdf
for page in pages:
    output.addPage(input1.getPage(page))

# write the output pdf to file
outputStream = file(sys.argv[1]+'-fr.pdf','wb')
output.write(outputStream)
outputStream.close()

print
