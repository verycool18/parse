import requests
from bs4 import BeautifulSoup
import io
URL = 'https://newsnow.co.uk/h/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
           'Accept': '*/*'}


def get_html(url, params=None):
    search = requests.get(url, headers=HEADERS, params=params)
    return search


def get_contact(html):
    soup = BeautifulSoup(html.text, features='html.parser')
    items = soup.find_all('div', class_='rs-newsbox')
    file = io.open('title.txt', 'w',encoding="utf-8")
    num_1 = 0
    for item in items:
        title = item.find('a', class_='rs-topic-heading__link')
        title_rub = item.find_all('a', class_='hll')

        if title is not None:
            num_1 += 1
            file.write(f'Title #{num_1} - {str(title.get_text())}\n')
        for i in title_rub:
            file.write(f'- {i.get_text()}\n')
    file.close()


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_contact(html)
    else:
        return ('Error')


parse()
