
import re

def extract_emails(text):
    emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', text)
    return emails

# Read text from a file
with open('text_document.txt', 'r') as file:
    text = file.read()

# Extract email addresses from the text
email_addresses = extract_emails(text)

# Print the extracted email addresses
for email in email_addresses:
    print(email)
