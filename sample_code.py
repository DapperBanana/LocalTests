
import re

def extract_emails_from_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return emails

file_path = 'sample_text.txt'
emails = extract_emails_from_text(file_path)

print("Email addresses found in the text document:")
for email in emails:
    print(email)
