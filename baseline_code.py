
# Simple text-based language translator

def translate_text(text, source_lang, target_lang):
    translations = {
        'hello': {
            'english': 'hello',
            'spanish': 'hola',
            'french': 'bonjour'
        },
        'goodbye': {
            'english': 'goodbye',
            'spanish': 'adiós',
            'french': 'au revoir'
        },
        'thank you': {
            'english': 'thank you',
            'spanish': 'gracias',
            'french': 'merci'
        }
    }

    # Check if the source and target languages are supported
    if source_lang not in translations['hello'] or target_lang not in translations['hello']:
        return "Unsupported languages"

    # Translate the text
    translated_text = translations.get(text.lower(), {}).get(target_lang)
    
    if translated_text:
        return translated_text
    else:
        return "Translation not found"

source_lang = 'english'
target_lang = 'spanish'

text = input("Enter the text to translate: ")

translated_text = translate_text(text, source_lang, target_lang)

print(f"Translated text: {translated_text}")
