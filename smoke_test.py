
# Basic text-based language translator

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
}

def translate_word(word, language):
    if word in translations:
        if language in translations[word]:
            return translations[word][language]
        else:
            return f"No translation found for {language}"
    else:
        return "Word not found in dictionary"
    
def main():
    print("Welcome to the basic text-based language translator!")
    
    while True:
        word = input("Enter a word to translate (or 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        
        language = input("Enter the target language (e.g. spanish, french, german): ")
        
        translation = translate_word(word.lower(), language.lower())
        print(f"The translation of '{word}' in {language} is '{translation}'\n")
    
    print("Thank you for using the translator. Goodbye!")

if __name__ == "__main__":
    main()
