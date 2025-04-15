
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    print("Basic Language Translator")
    print("-------------------------")
    
    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish): ")
    
    translated_text = translate_text(text, target_language)
    
    print(f"\nTranslated Text: {translated_text}")

if __name__ == "__main__":
    main()
