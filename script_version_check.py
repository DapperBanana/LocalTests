
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char) + shift
            if char.islower():
                if ascii_val > ord('z'):
                    ascii_val -= 26
            elif char.isupper():
                if ascii_val > ord('Z'):
                    ascii_val -= 26
            result += chr(ascii_val)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

if __name__ == "__main__":
    text = "Hello, World!"
    shift = 3

    encrypted_text = caesar_cipher_encrypt(text, shift)
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

    print("Original text:", text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
