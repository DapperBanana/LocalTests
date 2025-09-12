
translations = {
    "hello": {
        "spanish": "hola",
        "french": "bonjour",
        "german": "hallo"
    },
    "goodbye": {
        "spanish": "adios",
        "french": "au revoir",
        "german": "auf wiedersehen"
    }
}

def translate(word, language):
    if word.lower() in translations:
        if language.lower() in translations[word.lower()]:
            return translations[word.lower()][language.lower()]
    
    return "Translation not found"

def main():
    word = input("Enter a word to translate: ")
    language = input("Enter the language to translate to (spanish, french, or german): ")

    translation = translate(word, language)

    print(f"The translation of '{word}' in {language} is: {translation}")

if __name__ == "__main__":
    main()
