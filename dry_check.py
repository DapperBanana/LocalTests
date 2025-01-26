
import re

def extract_emails(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, text)
    return emails

# Read text document
with open('sample_text.txt', 'r') as file:
    text = file.read()

emails = extract_emails(text)

for email in emails:
    print(email)
