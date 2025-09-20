
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, options={'verify_signature': False})
        return True
    except jwt.InvalidTokenError:
        return False

# Test the function
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ._vPV0yHsoRtLtyjWItKegGJSanMmzZXJT_VT5RBzosI"
if is_valid_jwt(jwt_token):
    print("The token is a valid JWT.")
else:
    print("The token is not a valid JWT.")
