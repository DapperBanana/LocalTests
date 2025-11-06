
import PyPDF2

# Function to extract text content from a PDF file
def extract_text_from_pdf(pdf_file_path):
    text = ""
    pdf_file = open(pdf_file_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdfReader.numPages
    
    for page_num in range(num_pages):
        page = pdfReader.getPage(page_num)
        text += page.extract_text()
    
    pdf_file.close()
    return text

# Main program
pdf_file_path = "sample.pdf"
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text)
