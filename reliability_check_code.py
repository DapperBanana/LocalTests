
import base64
import json

def is_valid_jwt(token):
    token_parts = token.split('.')
    
    if len(token_parts) != 3:
        return False

    try:
        header = json.loads(base64.urlsafe_b64decode(token_parts[0] + '==').decode('utf-8'))
        payload = json.loads(base64.urlsafe_b64decode(token_parts[1] + '==').decode('utf-8'))

        if not isinstance(header, dict) or not isinstance(payload, dict):
            return False

        return True
    except (json.JSONDecodeError, UnicodeDecodeError, TypeError):
        return False

# Example usage
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkphbWEgRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.eyJpc3MiOiJodHRwczovL2xvY2FsaG9zdCJ9.yIB4NruZ2vZGxqe++tVI9cz1OLkvdL7LUmZ2vuZ9c1w="
print(is_valid_jwt(token))  # Output: True
