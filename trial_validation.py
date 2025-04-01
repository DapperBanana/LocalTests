
import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

def main():
    file_path = 'sample.txt'  # replace with the path to your text document
    with open(file_path, 'r') as file:
        text = file.read()
    
    emails = extract_emails(text)
    
    print("Email addresses found:")
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()
