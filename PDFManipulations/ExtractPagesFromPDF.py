from PyPDF2 import PdfReader, PdfWriter

#Replace with the name of the PDF file
pdf_file_path = 'InputFile.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfReader(pdf_file_path)

#Put the pages numbers, which you need to extract.
pages = [0, 1, 2, 3, 4, 5, 6, 7] 

#UnComment the below code, if you wish to have the whole document subset starting from page 5 to page 38
#pages = list(range(4, 37))

pdfWriter = PdfWriter()

for page_num in pages:
    pdfWriter.add_page(pdf.pages[page_num])

with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
    pdfWriter.write(f)
    f.close()

print('Selected subset of pages successfully')
