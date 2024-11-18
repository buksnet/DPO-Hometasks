from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from requests import get
from requests.exceptions import ConnectionError

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import pandas

CHOSEN_URL = "https://python.org"


def is_accessible(url: str):
    try:
        if urlopen(url):
            print("Страница найдена")
            return True
    except ConnectionError as e:
        print(f"Такая страница не существует {e}")
    except HTTPError as e:
        print(f"Не удаётся установить соединение: {e}")
    except URLError as e:
        print(f"Некорректный URL: {e}")
    return False


print('1.\n', is_accessible(CHOSEN_URL))


def check_for_SSH(url):
    if url.startswith('https://'):
        try:
            get(url)
            return True
        except Exception as e:
            print(e)
    return False


print('2.\n', check_for_SSH(CHOSEN_URL))


def python_site_stats():
    PYTHON_URL = "https://python.org"
    try:
        response = get(PYTHON_URL)
        print('3.\n', response.status_code, response.headers, response.url, response.history, response.encoding,
              response.reason, response.cookies, response.elapsed, response.request, response.content, sep='\n')
    except Exception as e:
        print('3.\n', e)


python_site_stats()


def get_robots_wikipedia():
    WIKI_URL = "https://en.wikipedia.org/"

    try:
        print('4.\n', get(WIKI_URL + 'robots.txt').content)
    except Exception as e:
        print('4.\n', e)


get_robots_wikipedia()


def get_header_from_example():
    EXAMPLE_URL = "http://www.example.com/"

    try:
        page_content = get(EXAMPLE_URL).content
        soup = BeautifulSoup(page_content, 'html.parser')
        print('5.\n', soup.h1)

    except Exception as e:
        print('5.\n', e)


get_header_from_example()


def get_all_wiki_headers():
    WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"

    try:
        page_content = get(WIKI_URL).content
        soup = BeautifulSoup(page_content, 'html.parser')

        print('6.', 'h1: ' + str(soup.find_all(name="h1")), 'h2: ' + str(soup.find_all(name="h2")),
              'h3: ' + str(soup.find_all(name="h3")), 'h4: ' + str(soup.find_all(name="h4")),
              'h5: ' + str(soup.find_all(name="h5")), 'h6: ' + str(soup.find_all(name="h6")), sep='\n')
    except Exception as e:
        print('6.\n', e)


get_all_wiki_headers()


def get_all_links_from_wiki():
    WIKI_URL = "https://en.wikipedia.org/wiki/Python"

    try:
        response = get(WIKI_URL)

        http_encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(response.content, is_html=True)
        encoding = html_encoding or http_encoding

        soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)

        print('7.\n')
        ind = 1
        for link in soup.find_all('a', href=True):
            print('    - ', ind, ':', sep='', end=' ')
            ind += 1
            print('    ', link['href'])

    except Exception as e:
        print('7.\n', e)


get_all_links_from_wiki()


def count_csv_table_rows():
    table = pandas.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv")
    print('8.\n', len(table))


count_csv_table_rows()
