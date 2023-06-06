import requests
from bs4 import BeautifulSoup
try:
    url = str(input('Paste link --> '))
    response = requests.get(url)
    if response.status_code == 200:
        result = BeautifulSoup(response.text, 'html.parser')
        title = result.select('p')
        for items in title:
            print(items.text)
    else:
        print("error connect")        
except ValueError:
    print("Please, paste link")
