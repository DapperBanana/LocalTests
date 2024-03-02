
# Basic text-based language translator

translations = {
    'hello': {
        'spanish': 'hola',
        'french': 'bonjour',
        'german': 'hallo'
    },
    'goodbye': {
        'spanish': 'adios',
        'french': 'au revoir',
        'german': 'auf wiedersehen'
    },
    'thank you': {
        'spanish': 'gracias',
        'french': 'merci',
        'german': 'danke'
    }
}

def translate(text, language):
    if text.lower() in translations:
        if language.lower() in translations[text.lower()]:
            return translations[text.lower()][language.lower()]
        else:
            return f"Translation for '{language}' not available"
    else:
        return "Text not found in translation dictionary"

def main():
    text = input("Enter the text to translate: ")
    language = input("Enter the language to translate to (e.g. spanish, french, german): ")
    
    translation = translate(text, language)
    print(f"Translation: {translation}")

if __name__ == "__main__":
    main()
