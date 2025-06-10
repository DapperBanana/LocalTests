
import re

def extract_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    
    return emails

def main():
    with open('sample_text.txt', 'r') as file:
        text = file.read()
        
    email_addresses = extract_email_addresses(text)
    
    if email_addresses:
        for email in email_addresses:
            print(email)
    else:
        print("No email addresses found in the text.")

if __name__ == "__main__":
    main()
