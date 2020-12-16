import requests
from bs4 import BeautifulSoup

URL = 'https://newsnow.co.uk/h/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
           'Accept': '*/*'}


def get_html(url, params=None):
    search = requests.get(url, headers=HEADERS, params=params)
    return search


def get_contact(html):
    soup = BeautifulSoup(html.text, features='html.parser')
    items = soup.find_all('div', class_='rs-topic-heading__row-1')

    title_list = []
    for item in items:
        title = item.find('a', 'rs-topic-heading__link js-topic-heading-link')
        if title is not None:
            title_list.append(title.get_text())
    file = open('title.txt', 'w')
    num = 0
    for i in title_list:
        num += 1
        file.write(f'Title #{num} - {i}\n')

    file.close()


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_contact(html)
    else:
        return ('Error')


parse()
