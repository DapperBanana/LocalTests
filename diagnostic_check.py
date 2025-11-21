
def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted_char = ord(char) + shift
            if char.islower():
                if shifted_char > ord('z'):
                    shifted_char -= 26
            elif char.isupper():
                if shifted_char > ord('Z'):
                    shifted_char -= 26
            encrypted_text += chr(shifted_char)
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted_char = ord(char) - shift
            if char.islower():
                if shifted_char < ord('a'):
                    shifted_char += 26
            elif char.isupper():
                if shifted_char < ord('A'):
                    shifted_char += 26
            decrypted_text += chr(shifted_char)
        else:
            decrypted_text += char
    
    return decrypted_text

text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print("Encrypted text: ", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text: ", decrypted_text)
