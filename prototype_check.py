
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

# Read the text file
with open('text_document.txt', 'r') as file:
    text_data = file.read()

# Extract email addresses
emails = extract_emails(text_data)

# Print the extracted email addresses
for email in emails:
    print(email)
