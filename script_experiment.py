
import re

# Read the text document
with open('text.txt', 'r') as file:
    text = file.read()

# Regular expression for email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all email addresses in the text
emails = re.findall(pattern, text)

# Print all email addresses found
for email in emails:
    print(email)
