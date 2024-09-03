
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

if __name__ == "__main__":
    file_name = "sample.txt"  # Replace with the name of your text document
    with open(file_name, 'r') as file:
        data = file.read()
        emails = extract_emails(data)
    
    print("Email addresses found in the document:")
    for email in emails:
        print(email)
