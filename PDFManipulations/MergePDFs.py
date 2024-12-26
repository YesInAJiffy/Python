import os
from PyPDF2 import PdfMerger

#All the files in the current directory, with PDF extension are selected.
x = [a for a in os.listdir() if a.endswith(".pdf")]
#The files are sorted, so that the order in which the files are merged is maintained.
x.sort()

merger = PdfMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)

print('Merge Completed')
