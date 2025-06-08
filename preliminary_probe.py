
# Dictionary containing translations for some common words
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
    },
    "thank you": {
        "spanish": "gracias",
        "french": "merci",
        "german": "danke"
    }
}

def translate_word(word, language):
    if word.lower() in translations:
        if language.lower() in translations[word.lower()]:
            return translations[word.lower()][language.lower()]
        else:
            return f"Translation not available for '{language}'"
    else:
        return f"'{word}' is not in the dictionary"

def main():
    word = input("Enter a word to translate: ")
    language = input("Enter a language to translate to (e.g. spanish, french, german): ")

    translation = translate_word(word, language)
    print(translation)

if __name__ == "__main__":
    main()
