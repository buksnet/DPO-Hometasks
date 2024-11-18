from itertools import cycle

from requests import get
from requests.exceptions import ConnectionError

from bs4 import BeautifulSoup


def fetch_imdb_html() -> bytes | None:
    IMDB_URL = "https://www.imdb.com/chart/top/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    try:
        response = get(IMDB_URL, headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(e)
    return None


def find_titles(page_content):
    soup = BeautifulSoup(page_content, features='html.parser')
    print(soup.prettify())
    titles = soup.find_all('h3', {'class': 'ipc-title__text'})
    print('-----------------------------------------------')

    for title in titles:
        print(title.text)
        print('-----------------------------------------------')


page_content = fetch_imdb_html()
find_titles(page_content)
