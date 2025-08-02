
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com/data-table-page'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

for row in data:
    print(row)
