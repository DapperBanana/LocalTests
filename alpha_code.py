
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

def main():
    pdf_file = 'sample.pdf'
    text = extract_text_from_pdf(pdf_file)
    print(text)

if __name__ == '__main__':
    main()
