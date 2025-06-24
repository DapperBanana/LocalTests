
def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            ascii_val = ord(char)
            if char.islower():
                encrypted_text += chr((ascii_val - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ascii_val - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
