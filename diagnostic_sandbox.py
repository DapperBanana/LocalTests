
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = caesar_cipher_encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
