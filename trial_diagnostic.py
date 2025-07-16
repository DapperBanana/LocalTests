
import PyPDF2

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_file = 'example.pdf'
    extracted_text = extract_text_from_pdf(pdf_file)
    print(extracted_text)
