
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

print("Welcome to the basic text-based language translator!")
text = input("Enter the text you want to translate: ")
target_language = input("Enter the target language (e.g. 'es' for Spanish, 'fr' for French): ")

translated_text = translate_text(text, target_language)
print("Translated text: ", translated_text)
