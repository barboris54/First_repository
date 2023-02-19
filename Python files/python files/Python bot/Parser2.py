import requests
from bs4 import BeautifulSoup as bs

LINK = 'https://ru.wordpress.org/themes/'


def get_html(link):
    request = requests.get(link)
    return request.text


def get_data(html):
    soup = bs(html, 'lxml')
    names = soup.find_all('article', class_="theme")
    for name in names:
        block_name = name.find('h3').text
        link = name.find('a',class_='url').get('href')
        print(block_name,link)


def main():
    link = LINK
    print(get_data(get_html(link)))


if __name__ == "__main__":
    main()
