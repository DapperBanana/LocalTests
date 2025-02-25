
# Dictionary containing translations for some common language pairs
translations = {
    "hello": {
        "english": "hello",
        "spanish": "hola",
        "french": "bonjour"
    },
    "goodbye": {
        "english": "goodbye",
        "spanish": "adios",
        "french": "au revoir"
    },
    "thank you": {
        "english": "thank you",
        "spanish": "gracias",
        "french": "merci"
    }
}

def translate_text(text, from_lang, to_lang):
    if text.lower() in translations.keys():
        if from_lang in translations[text]:
            return translations[text][to_lang]
        else:
            return "Translation not available for this language"
    else:
        return "Text not found in the dictionary"

# Main program
print("Welcome to the Language Translator!")
while True:
    user_input = input("Enter text to translate (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    from_lang = input("Enter the language of the text: ")
    to_lang = input("Enter the language to translate to: ")
    
    translated_text = translate_text(user_input, from_lang, to_lang)
    print(f"Translated text: {translated_text}")
