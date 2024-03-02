
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
