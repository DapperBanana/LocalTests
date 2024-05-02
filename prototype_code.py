
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, world!"
shift = 3
encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
