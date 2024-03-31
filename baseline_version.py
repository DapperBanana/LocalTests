
def caesar_cipher_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A' if char.isupper() else 'a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, key):
    return caesar_cipher_encrypt(text, -key)

text = "Hello, World!"
key = 3

encrypted_text = caesar_cipher_encrypt(text, key)
decrypted_text = caesar_cipher_decrypt(encrypted_text, key)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
