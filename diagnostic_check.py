
def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char

    return result

def caesar_decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char

    return result

text = "Hello, World!"
key = 3

encrypted_text = caesar_encrypt(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
