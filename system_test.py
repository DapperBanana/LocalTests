
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.InvalidTokenError:
        return False

# Test the function with a sample JWT
sample_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImlhdCI6MTYwMDc1Njk5OH0.Z2wi6d5h9oYeb4ZjZFgPv5eVr5dXU7AO0wb9e_FAhaM"
print(is_valid_jwt(sample_jwt))
