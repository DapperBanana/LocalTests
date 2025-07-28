
import re

def extract_emails(text):
    pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    emails = re.findall(pattern, text)
    return emails

# Read the text document
with open('sample.txt', 'r') as file:
    text = file.read()

# Extract emails from the text document
emails = extract_emails(text)

# Print the extracted emails
for email in emails:
    print(email)
