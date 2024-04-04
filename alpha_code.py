
import base64
import json

def is_valid_jwt(token):
    parts = token.split('.')
    
    if len(parts) != 3:
        return False
        
    header = parts[0]
    payload = parts[1]
    
    try:
        json.loads(base64.urlsafe_b64decode(header + '==').decode('utf-8'))
        json.loads(base64.urlsafe_b64decode(payload + '==').decode('utf-8'))
        return True
    except:
        return False

# Example usage
jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
result = is_valid_jwt(jwt_token)

if result:
    print("The provided string is a valid JSON Web Token (JWT)")
else:
    print("The provided string is not a valid JSON Web Token (JWT)")
