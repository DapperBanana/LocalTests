
import requests
from bs4 import BeautifulSoup

# Function to scrape information from a website
def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract information from the parsed HTML
        # Replace 'h1' and 'p' with the desired HTML tags to extract
        headings = soup.find_all('h1')
        paragraphs = soup.find_all('p')
        
        # Print the extracted information
        print("HEADINGS:")
        for heading in headings:
            print(heading.text.strip())
        
        print("\nPARAGRAPHS:")
        for paragraph in paragraphs:
            print(paragraph.text.strip())
    else:
        print("Error: Could not retrieve the website content")

# URL of the website to scrape
url = 'https://example.com'

# Scrape the website information
scrape_website(url)
