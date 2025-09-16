
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False

# Test the function
token1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikphc29uIiwiaWF0IjoxNTE2MjM5MDIyfQ.AG-K8B45X6IJzXgyTG4tD2xkCC9AFrY7ByVE9CKH1ck"
token2 = "invalid_token"

if is_valid_jwt(token1):
    print("Token 1 is a valid JWT.")
else:
    print("Token 1 is not a valid JWT.")

if is_valid_jwt(token2):
    print("Token 2 is a valid JWT.")
else:
    print("Token 2 is not a valid JWT.")
