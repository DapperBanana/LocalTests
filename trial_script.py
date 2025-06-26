
from googletrans import Translator

# Create a translator object
translator = Translator()

def translate_text(text, dest_lang='en'):
    # Detect the language of the input text
    detected_lang = translator.detect(text).lang
    
    if detected_lang == dest_lang:
        return text
    else:
        # Translate the text to the destination language
        translated_text = translator.translate(text, dest=dest_lang).text
        return translated_text

# Input text to be translated
text = input("Enter text to be translated: ")

# Destination language code (e.g. 'fr' for French, 'es' for Spanish)
dest_lang = input("Enter destination language code: ")

# Translate the input text
translated_text = translate_text(text, dest_lang)

print(f"Translated text: {translated_text}")
