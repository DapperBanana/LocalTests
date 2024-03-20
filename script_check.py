letion(id='chatcmpl-94ej6hnDv4pHHM0BumUbMw3dXF2WE', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    # Send a get request to the specified URL
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract information from the HTML content
    title = soup.title.text
    headings = [heading.text for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    
    # Print the extracted information
    print("Title: ", title)
    print("Headings: ", headings)

url = "https://example.com"
web_scraper(url)', role='assistant', function_call=None, tool_calls=None))], created=1710896892, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=147, prompt_tokens=25, total_tokens=172)