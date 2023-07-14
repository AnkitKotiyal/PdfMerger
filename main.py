import PyPDF2 as py

my_pdf_files=["sample1.pdf","sample2.pdf"]# A list containing all pdf which we want to merge together

merger=py.PdfMerger()
for fileNames in my_pdf_files:
    pdfFile=open(fileNames,'rb')
    pdfReader=py.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('Merged.pdf')


