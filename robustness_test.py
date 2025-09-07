
import base64
import json

def is_valid_jwt(token):
    parts = token.split('.')
    if len(parts) != 3:
        return False

    header = parts[0]
    payload = parts[1]
    signature = parts[2]

    try:
        header = json.loads(base64.urlsafe_b64decode(header + '===='))
        payload = json.loads(base64.urlsafe_b64decode(payload + '===='))
    except:
        return False

    return True

# Test the function
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvZSBEb2UiLCJpYXQiOjE1MTYyMzkwMjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
if is_valid_jwt(token):
    print("Valid JWT")
else:
    print("Invalid JWT")
