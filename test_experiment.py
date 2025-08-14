
import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

# Open the text document
with open('text_document.txt', 'r') as file:
    text = file.read()

# Extract email addresses from the text
emails = extract_emails(text)

# Print the extracted email addresses
for email in emails:
    print(email)
