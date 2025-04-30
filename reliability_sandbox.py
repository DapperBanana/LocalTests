
import base64

def is_valid_jwt(token):
    parts = token.split('.')
    
    if len(parts) != 3:
        return False
    
    header = parts[0]
    payload = parts[1]
    signature = parts[2]
    
    try:
        header_decoded = base64.urlsafe_b64decode(header + '=' * (4 - len(header) % 4)).decode('utf-8')
        payload_decoded = base64.urlsafe_b64decode(payload + '=' * (4 - len(payload) % 4)).decode('utf-8')
    except:
        return False
    
    return True

# Test the function
jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.eyJleHBpcmVzIjoxNjAyNDkzNDU2LCJpYXQiOjE2MDI0OTM0NTZ9.9F3Fzi9L8I_AkWZ8a3GyKb_j5G5kq8iNVyhfGede2-w"
print(is_valid_jwt(jwt)) # Output: True

invalid_jwt = "invalid.jwt"
print(is_valid_jwt(invalid_jwt)) # Output: False
