
import re

# Function to extract email addresses from text
def extract_emails(text):
    # Regular expression to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Find all email addresses in the text
    emails = re.findall(email_pattern, text)
    
    return emails

# Read text document
with open('text_document.txt', 'r') as file:
    text = file.read()

# Extract email addresses from text
emails = extract_emails(text)

# Print all email addresses
for email in emails:
    print(email)
