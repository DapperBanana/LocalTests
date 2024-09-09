
# Dictionary mapping languages to their translations
translations = {
    "english": {
        "hello": "Hello",
        "goodbye": "Goodbye",
        "thank you": "Thank you",
    },
    "spanish": {
        "hello": "Hola",
        "goodbye": "Adiós",
        "thank you": "Gracias",
    },
    "french": {
        "hello": "Bonjour",
        "goodbye": "Au revoir",
        "thank you": "Merci",
    }
}

def translate_text(input_text, source_lang, target_lang):
    source_dict = translations.get(source_lang.lower())
    if source_dict is None:
        return "Source language not supported"

    target_dict = translations.get(target_lang.lower())
    if target_dict is None:
        return "Target language not supported"

    translated_text = []
    words = input_text.lower().split()
    
    for word in words:
        translated_word = target_dict.get(source_dict.get(word))
        if translated_word:
            translated_text.append(translated_word)

    return " ".join(translated_text)

def main():
    source_lang = input("Enter source language: ")
    target_lang = input("Enter target language: ")
    input_text = input("Enter text to translate: ")

    translated_text = translate_text(input_text, source_lang, target_lang)
    print("Translated text:", translated_text)

if __name__ == "__main__":
    main()
