
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            encrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")
