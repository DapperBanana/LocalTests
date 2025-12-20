using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        Console.Write("Enter text to translate: ");
        string text = Console.ReadLine();

        Console.Write("Enter target language code (e.g., 'en' for English, 'fr' for French): ");
        string targetLanguage = Console.ReadLine();

        try
        {
            string translatedText = await TranslateTextAsync(text, targetLanguage);
            Console.WriteLine($"Translated text: {translatedText}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static async Task<string> TranslateTextAsync(string text, string targetLanguage)
    {
        // Note: Replace 'YOUR_API_KEY' with a valid API key for the translation service
        string apiKey = "YOUR_API_KEY";
        string url = $"https://api.mymemory.translated.net/get?q={Uri.EscapeDataString(text)}&langpair=en|{targetLanguage}";

        using (HttpClient client = new HttpClient())
        {
            HttpResponseMessage response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();

            string jsonResponse = await response.Content.ReadAsStringAsync();
            // Basic parsing without external JSON libraries
            // Extract translated text from response
            string marker = "\"translatedText\":\"";
            int startIndex = jsonResponse.IndexOf(marker) + marker.Length;
            int endIndex = jsonResponse.IndexOf("\"", startIndex);
            if (startIndex < marker.Length || endIndex < startIndex)
                throw new Exception("Translation failed.");

            string translatedText = jsonResponse.Substring(startIndex, endIndex - startIndex);
            // Decode any escaped characters
            translatedText = System.Net.WebUtility.HtmlDecode(translatedText);
            return translatedText;
        }
    }
}