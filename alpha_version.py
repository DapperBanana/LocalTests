
import requests
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com/html/html_tables.asp'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

for row in data:
    print(row)
