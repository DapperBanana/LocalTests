
import re

def is_valid_jwt(token):
    jwt_regex = r'^[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$'
    
    if re.match(jwt_regex, token):
        return True
    else:
        return False

# Test the function with a sample JWT token
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
if is_valid_jwt(token):
    print("The given string is a valid JWT.")
else:
    print("The given string is not a valid JWT.")
