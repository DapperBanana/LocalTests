
def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
            
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
            
    return decrypted_text

text = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
