
import PyPDF2

# Open the PDF file in read-binary mode
with open('sample.pdf', 'rb') as pdf_file:
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Initialize a variable to store the text content of the PDF file
    text_content = ''

    # Loop through each page in the PDF file
    for page_num in range(pdf_reader.numPages):
        # Get the page object
        page = pdf_reader.getPage(page_num)

        # Extract text from the page
        text_content += page.extract_text()

# Print the extracted text content
print(text_content)
