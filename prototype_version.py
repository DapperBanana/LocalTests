
import jwt

def check_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.InvalidTokenError:
        return False

# Test the function with a JWT token
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.niIif6RyVjUKnXUuXAw5WdH5Uifu-l20c5cB11OA6GA"
if check_valid_jwt(token):
    print("The token is a valid JWT.")
else:
    print("The token is not a valid JWT.")
