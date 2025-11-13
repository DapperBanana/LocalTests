
import re

# Read the text document
with open("text_document.txt", "r") as file:
    text = file.read()

# Regular expression for matching email addresses
pattern = r'[\w\.-]+@[\w\.-]+'

# Find all email addresses in the text
emails = re.findall(pattern, text)

# Print all email addresses
for email in emails:
    print(email)
