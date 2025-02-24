
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_text += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

text = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
