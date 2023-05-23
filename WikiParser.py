import requests
from bs4 import BeautifulSoup


url = 'https://uk.wikipedia.org/wiki/%D0%94%D0%B8%D0%BD%D0%BE%D0%B7%D0%B0%D0%B2%D1%80%D0%B8' # потрібно вставити посилання сторінки

response = requests.get(url)

if response.status_code == 200:
    result = BeautifulSoup(response.text, 'html.parser')
    title = result.find('h1').text

    print(f"Заголовок сторінки: {title}")
else:
    print("error connect")
