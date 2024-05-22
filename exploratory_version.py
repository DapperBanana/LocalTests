
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

file_path = "example.pdf"
extracted_text = extract_text_from_pdf(file_path)
print(extracted_text)
