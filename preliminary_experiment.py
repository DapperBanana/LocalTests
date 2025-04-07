
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    
    return text

# Replace 'example.pdf' with the path to your PDF file
pdf_file = 'example.pdf'

extracted_text = extract_text_from_pdf(pdf_file)
print(extracted_text)
