
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ''
    
    # Open the PDF file in read-binary mode
    with open(pdf_file, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        
        # Iterate through each page of the PDF
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            text += page.extract_text()
            
    return text

if __name__ == "__main__":
    pdf_file = 'sample.pdf'
    extracted_text = extract_text_from_pdf(pdf_file)
    
    print(extracted_text)
