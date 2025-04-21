
from bs4 import BeautifulSoup
import requests

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'id': 'customers'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)
