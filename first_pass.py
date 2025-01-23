
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
