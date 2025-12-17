using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

namespace TextTranslator
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Enter text to translate:");
            string text = Console.ReadLine();

            Console.WriteLine("Enter target language code (e.g., 'en' for English, 'es' for Spanish):");
            string targetLanguage = Console.ReadLine();

            string apiKey = "YOUR_API_KEY"; // Replace with your actual API key
            string sourceLanguage = "auto";

            string translatedText = await TranslateTextAsync(text, sourceLanguage, targetLanguage, apiKey);
            Console.WriteLine($"Translated Text: {translatedText}");
        }

        static async Task<string> TranslateTextAsync(string text, string sourceLang, string targetLang, string apiKey)
        {
            using (HttpClient client = new HttpClient())
            {
                string url = $"https://api.mymemory.translated.net/get?q={Uri.EscapeDataString(text)}&langpair={sourceLang}|{targetLang}";
                HttpResponseMessage response = await client.GetAsync(url);
                if (response.IsSuccessStatusCode)
                {
                    string jsonResponse = await response.Content.ReadAsStringAsync();
                    JObject json = JObject.Parse(jsonResponse);
                    return json["responseData"]["translatedText"].ToString();
                }
                else
                {
                    return "Error in translation API.";
                }
            }
        }
    }
}