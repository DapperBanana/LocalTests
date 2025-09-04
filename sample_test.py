
import re

def extract_emails(text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(regex, text)
    return emails

def main():
    with open('sample_text.txt', 'r') as file:
        text = file.read()
    
    emails = extract_emails(text)
    
    print("Email addresses found:")
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()
