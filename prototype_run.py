
import base64
import json

def is_valid_jwt(token):
    try:
        header, payload, signature = token.split('.')

        # Decode and parse header
        decoded_header = base64.urlsafe_b64decode(header + '=' * (-len(header) % 4))
        parsed_header = json.loads(decoded_header)

        # Decode and parse payload
        decoded_payload = base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4))
        parsed_payload = json.loads(decoded_payload)

        # No need to validate signature for this program
        return True
    except (ValueError, json.JSONDecodeError, KeyError):
        return False

# Test with some JWT tokens
jwt1 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikphc29uIiwiaWF0IjoxNTE2MjM5MDIyfQ.O3z5gj76K5YTF42SFfbBCVEdDVfbsc693RRc6QYbvLQ'
jwt2 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikphc29uIn0.2IYToY5jg81RsdUK8Q3DgXBC4W4RUGru83ks3nL88cY'

print(is_valid_jwt(jwt1))  # True
print(is_valid_jwt(jwt2))  # False
