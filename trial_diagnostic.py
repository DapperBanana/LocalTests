
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

text = """
Hello, my email address is john.doe@example.com and my colleague's email address is jane_smith123@gmail.com.
Please contact us at these email addresses for further information.
"""

emails = extract_emails(text)

for email in emails:
    print(email)
