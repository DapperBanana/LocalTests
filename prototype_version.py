
# English to Spanish Translator

# Dictionary mapping English words to their Spanish translation
translator = {
    "hello": "hola",
    "goodbye": "adios",
    "thank you": "gracias",
    "yes": "si",
    "no": "no"
}

def translate_word(word):
    if word.lower() in translator:
        return translator[word.lower()]
    else:
        return "Translation not found"

def main():
    print("Welcome to the English to Spanish translator!")
    while True:
        word = input("Enter an English word to translate (or 'q' to quit): ")
        if word.lower() == 'q':
            break
        translation = translate_word(word)
        print(f"{word} in Spanish is: {translation}")

if __name__ == "__main__":
    main()
