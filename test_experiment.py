
import base64
import json

def is_valid_jwt(token):
    segments = token.split('.')
    
    if len(segments) != 3:
        return False
    
    try:
        header = json.loads(base64.urlsafe_b64decode(segments[0] + '==').decode('utf-8'))
        payload = json.loads(base64.urlsafe_b64decode(segments[1] + '==').decode('utf-8'))
        
        return True
    except (json.JSONDecodeError, base64.binascii.Error):
        return False

# Test the function
jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
if is_valid_jwt(jwt):
    print('The given string is a valid JSON Web Token (JWT)')
else:
    print('The given string is not a valid JSON Web Token (JWT)')
