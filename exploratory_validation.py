
def encrypt(text, key):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)

text = "Hello, World!"
key = 3

encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
