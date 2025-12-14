// Note: To analyze sentiment in Python, you typically use libraries like TextBlob or NLTK. 
// Since you requested C# code, here's an example using the Azure Text Analytics SDK as a common approach for sentiment analysis in C#.

using System;
using Azure;
using Azure.AI.TextAnalytics;

class Program
{
    static void Main()
    {
        // Replace with your Azure endpoint and API key
        string endpoint = "https://<your-text-analytics-resource>.cognitiveservices.azure.com/";
        string apiKey = "<your-api-key>";

        var client = new TextAnalyticsClient(new Uri(endpoint), new AzureKeyCredential(apiKey));

        Console.WriteLine("Enter the text for sentiment analysis:");
        string inputText = Console.ReadLine();

        DocumentSentiment sentiment = client.AnalyzeSentiment(inputText);

        Console.WriteLine($"Sentiment: {sentiment.Sentiment}");
        Console.WriteLine($"Positive: {sentiment.ConfidenceScores.Positive:0.00}");
        Console.WriteLine($"Neutral: {sentiment.ConfidenceScores.Neutral:0.00}");
        Console.WriteLine($"Negative: {sentiment.ConfidenceScores.Negative:0.00}");
    }
}