from PyPDF2 import PyPDF2


with open('1.pdf', 'rb') as pdf_file: 
    pdf_reader = PyPDF2.PdfFileReader(pdf_file) 
    # printing first page contents
    pdf_page = pdf_reader.getPage(0) 
    print(pdf_page.extractText()) # reading all the pages content one by one
    for page_num in range(pdf_reader.numPages):
        pdf_page = pdf_reader.getPage(page_num) 
        print(pdf_page.extractText())