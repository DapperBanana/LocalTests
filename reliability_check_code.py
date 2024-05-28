
# Import the Translator class from googletrans module
from googletrans import Translator

# Create an instance of Translator
translator = Translator()

print("Welcome to the Text-based Language Translator!")

# Get input text from user
input_text = input("Enter the text you want to translate: ")

# Get the target language from user
target_lang = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")

# Translate the input text to the target language
translated_text = translator.translate(input_text, dest=target_lang)

# Print the translated text
print("Translated Text: ", translated_text.text)
