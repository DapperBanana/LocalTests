
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.strip()

# Example usage
pdf_path = "example.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
