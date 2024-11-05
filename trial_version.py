
# dictionary mapping languages to their translations
translations = {
    "english": {"hello": "hola", "goodbye": "adios", "thank you": "gracias"},
    "spanish": {"hola": "hello", "adios": "goodbye", "gracias": "thank you"}
}

def translate_text(input_text, input_language, output_language):
    if input_language in translations and output_language in translations:
        translation_dict = translations[input_language]
        translated_text = translation_dict.get(input_text, "Translation not found")
        
        output_translation_dict = translations[output_language]
        output_text = output_translation_dict.get(translated_text, "Translation not found")
        
        return output_text
    else:
        return "Language not supported"

# user input
input_text = input("Enter text to translate: ")
input_language = input("Enter input language (english/spanish): ").lower()
output_language = input("Enter output language (english/spanish): ").lower()

translated_text = translate_text(input_text, input_language, output_language)
print("Translated text: ", translated_text)
