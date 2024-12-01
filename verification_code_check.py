
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_char = char
        encrypted_text += new_char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
