
import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('example.pdf', 'rb')

# Create a PdfFileReader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

text = ''

# Loop through each page in the PDF file
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(text)
