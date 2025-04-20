
from bs4 import BeautifulSoup
import requests

# URL of the web page containing the table
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

# Make a GET request to fetch the raw HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML content
table = soup.find('table', {'class': 'wikitable sortable'})

# Extract data from the table
rows = table.find_all('tr')
for row in rows:
    data = row.find_all('td')
    if len(data) > 0:
        country = data[1].text.strip()
        population = data[2].text.strip()
        print(f'Country: {country}, Population: {population}')
