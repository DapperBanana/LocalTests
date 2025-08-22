
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def main():
    with open('text_document.txt', 'r') as file:
        text = file.read()
        emails = extract_emails(text)
        
    print("Email addresses found in the text document:")
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()
