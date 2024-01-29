
import PyPDF2

def extract_text_from_pdf(filename):
    text = ""
    with open(filename, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Iterate over each page in the PDF file
        for page_num in range(len(pdf_reader.pages)):
            # Extract the text from each page
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    return text

# Usage example
filename = 'example.pdf'
text_content = extract_text_from_pdf(filename)
print(text_content)
