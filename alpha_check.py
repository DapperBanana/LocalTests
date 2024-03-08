
import re

def extract_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+'  # Regular expression pattern for detecting email addresses
    emails = re.findall(pattern, text)
    return emails

if __name__ == "__main__":
    with open('sample_text.txt', 'r') as file:
        text = file.read()
    
    all_emails = extract_emails(text)
    for email in all_emails:
        print(email)
