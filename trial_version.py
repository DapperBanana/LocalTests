
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Original text: ", text)
print("Encrypted text: ", encrypted_text)
print("Decrypted text: ", decrypted_text)
