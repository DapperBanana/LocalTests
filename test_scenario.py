
def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")
