
import re

# Function to extract email addresses from a text document
def extract_emails_from_text(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

# Read the text document
with open('sample.txt', 'r') as file:
    text = file.read()

# Extract email addresses from the text document
emails = extract_emails_from_text(text)

# Print the extracted email addresses
for email in emails:
    print(email)
