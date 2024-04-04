
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

def translate_text(text, target_language):
    translated_text = translations.get(text, {}).get(target_language)
    if translated_text:
        return translated_text
    else:
        return "Translation not available for that text."

if __name__ == "__main__":
    while True:
        input_text = input("Enter text to translate: ")
        if input_text.lower() == "exit":
            break
        target_language = input("Enter target language (spanish/french/german): ")
        translation = translate_text(input_text.lower(), target_language)
        print(f"Translation: {translation}")
