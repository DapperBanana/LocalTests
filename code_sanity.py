
import jwt

def is_valid_jwt(jwt_string):
    try:
        jwt.decode(jwt_string, verify=False) # Decode the JWT without verification
        return True
    except jwt.exceptions.DecodeError:
        return False

# Test the function
jwt_string = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.Tn6pR9Y40CquI1OKYO82sOoCb7SWi_BrwxX82svwN2c"
print(is_valid_jwt(jwt_string))
