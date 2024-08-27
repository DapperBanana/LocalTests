
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
    # Add more translations as needed
}

def translate(text, target_language):
    if text.lower() in translations:
        if target_language.lower() in translations[text.lower()]:
            return translations[text.lower()][target_language.lower()]
        else:
            return "Translation not available for {} to {}".format(text, target_language)
    else:
        return "Text not found in dictionary"

text = input("Enter the text to translate: ")
target_language = input("Enter the target language (e.g. spanish, french, german): ")

translation = translate(text, target_language)
print(translation)
