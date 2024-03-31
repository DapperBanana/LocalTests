
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
            
    return text

# Replace 'example.pdf' with the path to the PDF file you want to extract text from
file_path = 'example.pdf'
extracted_text = extract_text_from_pdf(file_path)

print(extracted_text)
