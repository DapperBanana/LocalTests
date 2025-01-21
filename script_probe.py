
def caesar_encrypt(text, key):
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

text = "Hello, World!"
key = 3

encrypted_text = caesar_encrypt(text, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
