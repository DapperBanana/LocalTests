
from bs4 import BeautifulSoup
import requests

# Function to extract data from HTML tables in a web page
def extract_data_from_table(url):
    # Make a GET request to the webpage
    response = requests.get(url)
    
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the tables in the webpage
    tables = soup.find_all('table')
    
    # Extract data from each table
    for table in tables:
        # Find all the rows in the table
        rows = table.find_all('tr')
        
        # Extract and print data from each row
        for row in rows:
            # Find all the cells in the row
            cells = row.find_all(['td', 'th'])
            
            # Extract and print data from each cell
            for cell in cells:
                print(cell.text.strip())
            print('--------')
            
# URL of the webpage with the table
url = 'https://example.com/table'

# Call the function to extract data from the table
extract_data_from_table(url)
