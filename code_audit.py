
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    
    return text

# Specify the path to the PDF file you want to extract text from
pdf_file = "example.pdf"

extracted_text = extract_text_from_pdf(pdf_file)
print(extracted_text)
