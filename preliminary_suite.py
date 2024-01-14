
from googletrans import Translator

def translate_text(text, source_language, target_language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src=source_language, dest=target_language)
    return translation.text

source_lang = input("Enter the source language: ")
target_lang = input("Enter the target language: ")
text = input("Enter the text to translate: ")

translated_text = translate_text(text, source_lang, target_lang)
print(f"Translated Text: {translated_text}")
