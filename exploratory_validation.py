
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf = PyPDF2.PdfFileReader(file)
        num_pages = pdf.getNumPages()
        
        for page_number in range(num_pages):
            page = pdf.getPage(page_number)
            text += page.extract_text()
    
    return text

# Specify the path to the PDF file
pdf_file = "sample.pdf"

# Extract text content from the PDF file
text_content = extract_text_from_pdf(pdf_file)

# Print the extracted text content
print(text_content)
