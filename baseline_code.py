
import re

def extract_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+'
    emails = re.findall(pattern, text)
    return emails

def main():
    file_path = 'sample_text_document.txt'
    with open(file_path, 'r') as file:
        text = file.read()
        emails = extract_emails(text)
        
        for email in emails:
            print(email)

if __name__ == '__main__':
    main()
