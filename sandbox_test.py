
from bs4 import BeautifulSoup
import requests

# URL of the web page
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the web page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the desired data
table = soup.find('table', {'class': 'wikitable'})

# Extract data from the table
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    country = cols[0].text.strip()
    population = cols[1].text.strip()
    data.append((country, population))

# Print the extracted data
for country, population in data:
    print(f'{country}: {population}')
