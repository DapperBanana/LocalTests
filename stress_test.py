
def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


text = input("Enter the text: ")
key = int(input("Enter the shift key: "))

# Encrypt the text
encrypted_text = caesar_encrypt(text, key)
print("Encrypted text:", encrypted_text)

# Decrypt the text
decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
