
def caesar_cipher(text, key, mode):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_letter = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                shifted_letter = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result += shifted_letter
        else:
            result += char

    return result

text = "Hello, World!"
key = 3
encrypted_text = caesar_cipher(text, key, 'encrypt')
decrypted_text = caesar_cipher(encrypted_text, key, 'decrypt')

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
