
import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_file_path = "sample.pdf"
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)
