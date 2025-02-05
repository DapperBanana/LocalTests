
import base64

def is_valid_jwt(token):
    parts = token.split('.')
    
    if len(parts) != 3:
        return False
    
    encoded_payload = parts[1]
    
    try:
        decoded_payload = base64.urlsafe_b64decode(encoded_payload + '=' * (4 - len(encoded_payload) % 4))
        return True
    except:
        return False

# Test the function
jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.U8rPfL9Jeqi4Fhm8GfJ5dql92l6ImJVbQvJ3_0N4HkQ'
print(is_valid_jwt(jwt)) # Output: True

invalid_jwt = 'invalid.token'
print(is_valid_jwt(invalid_jwt)) # Output: False
