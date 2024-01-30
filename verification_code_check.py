
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

# Test encryption
text = "Hello, World!"
shift = 3
encrypted_text = encrypt(text, shift)
print(f"Encrypted text: {encrypted_text}")

# Test decryption
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")
