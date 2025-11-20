
from googletrans import Translator

def translate_text(text, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text

text = input("Enter text to translate from English to French: ")
translated_text = translate_text(text, 'fr')
print("Translated text: ", translated_text)
