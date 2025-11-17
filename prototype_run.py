
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char)
            if char.islower():
                encrypted_text += chr((ascii_val - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ascii_val - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char)
            if char.islower():
                decrypted_text += chr((ascii_val - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ascii_val - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
