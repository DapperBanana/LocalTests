
import PyPDF2

# Open the PDF file in read-binary mode
with open('sample.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)

    # Initialize an empty string to store the extracted text
    text_content = ''

    # Iterate through each page of the PDF
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text_content += page.extract_text()

# Print the extracted text content
print(text_content)
