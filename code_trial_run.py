
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
