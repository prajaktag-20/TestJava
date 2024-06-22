import requests
import markdown
from bs4 import BeautifulSoup


def fetch_wiki_table_data(url):
    wiki_url = 'https://github.com/prajaktag-20/TestJava/wiki/Home'
    # Fetch the wiki page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {url}")
        return None
    
    # Parse Markdown content using BeautifulSoup
    html_content = markdown.markdown(response.text)
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    # Assuming there's only one table, process it
    if tables:
        table = tables[0]  # Get the first table found
        
        # Extract table headers
        headers = [header.text.strip() for header in table.find_all('th')]
        
        # Extract table data rows
        table_data = []
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the first row (header row)
            row_data = [data.text.strip() for data in row.find_all('td')]
            table_data.append(dict(zip(headers, row_data)))
        
        return table_data
    else:
        print("No tables found on the page.")
        return None

