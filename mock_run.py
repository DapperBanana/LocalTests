
import re

def extract_email_addresses(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

if __name__ == "__main__":
    file_path = "sample_text.txt"
    
    with open(file_path, 'r') as file:
        text = file.read()
    
    email_addresses = extract_email_addresses(text)
    
    if email_addresses:
        print("Email addresses found in the text document:")
        for email in email_addresses:
            print(email)
    else:
        print("No email addresses found in the text document.")
