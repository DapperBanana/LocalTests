
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + key) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)

if __name__ == "__main__":
    text = "Hello, World!"
    key = 3

    encrypted_text = encrypt(text, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)
