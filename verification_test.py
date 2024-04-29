
import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.getNumPages()
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_file_path = "example.pdf"
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)
