
def caesar_cipher(text, key, encrypt=True):
    result = ""
    shift = key % 26
    
    if not encrypt:
        shift = -shift
        
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
            
    return result

def main():
    text = "Hello, World!"
    key = 3
    
    encrypted_text = caesar_cipher(text, key)
    decrypted_text = caesar_cipher(encrypted_text, key, encrypt=False)
    
    print("Original text:", text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
