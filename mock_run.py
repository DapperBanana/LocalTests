
import re

def extract_emails(text):
    # regex pattern for email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # find all email addresses in the text
    emails = re.findall(pattern, text)
    
    return emails

# read text document
with open('sample_document.txt', 'r') as file:
    text = file.read()

# extract email addresses from the text
emails = extract_emails(text)

print("Email addresses found in the text document:")
for email in emails:
    print(email)
