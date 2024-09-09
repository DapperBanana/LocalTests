
import re

def extract_emails_from_text(text):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails

def main():
    with open('text_document.txt', 'r') as file:
        text = file.read()
        
    email_addresses = extract_emails_from_text(text)
    
    for email in email_addresses:
        print(email)

if __name__ == "__main__":
    main()
