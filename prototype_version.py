
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        num_pages = pdf.getNumPages()
        
        for page_num in range(num_pages):
            page = pdf.getPage(page_num)
            text += page.extract_text()
    
    return text

pdf_file = "sample.pdf"
extracted_text = extract_text_from_pdf(pdf_file)
print(extracted_text)
