
import re

def extract_emails(file_path):
    emails = []
    
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
            emails.extend(matches)
    
    return emails

file_path = 'sample_text.txt'
emails = extract_emails(file_path)

for email in emails:
    print(email)
