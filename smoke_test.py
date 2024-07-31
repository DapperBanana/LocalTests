
def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(text, key):
    return caesar_cipher(text, -key)

text = "Hello, World!"
key = 3

encrypted_text = caesar_cipher(text, key)
decrypted_text = decrypt_caesar_cipher(encrypted_text, key)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
