
import re

def extract_emails(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Read the text document
with open('sample.txt', 'r') as file:
    data = file.read()

# Extract email addresses from the text
emails = extract_emails(data)

# Print the extracted email addresses
for email in emails:
    print(email)
