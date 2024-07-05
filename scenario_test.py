letion(id='chatcmpl-9hQw3eQZylIed1mRSJ0aIfwzDEA3T', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.find_all('h2')

for title in titles:
    print(title.text)", role='assistant', function_call=None, tool_calls=None))], created=1720138671, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=56, prompt_tokens=25, total_tokens=81)