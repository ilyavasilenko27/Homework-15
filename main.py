from PyPDF2 import PyPDF2

new_pdf = PyPDF2.PdfFileReader("1.pdf")
print(new_pdf.getDocumentInfo())
print(new_pdf.getNumPages())

