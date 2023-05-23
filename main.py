import requests
from bs4 import BeautifulSoup


url = '' <-- # Paste the page link to see the title


response = requests.get(url)

if response.status_code == 200:
    result = BeautifulSoup(response.text, 'html.parser')
    title = result.find('h1').text

    print(f"Заголовок сторінки: {title}")
else:
    print("error connect")
