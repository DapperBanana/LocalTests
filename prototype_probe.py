
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

# Read the text document
file_path = 'sample_text.txt'
with open(file_path, 'r') as file:
    text = file.read()

# Extract email addresses from the text
email_addresses = extract_emails(text)

# Print the extracted email addresses
for email in email_addresses:
    print(email)
