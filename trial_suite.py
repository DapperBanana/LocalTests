
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    result = translator.translate(text, dest=target_language)
    return result.text

if __name__ == "__main__":
    print("Welcome to the Basic Text-based Language Translator")
    
    text = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g. 'es' for Spanish, 'fr' for French): ")
    
    translated_text = translate_text(text, target_language)
    print(f"Translated text: {translated_text}")
