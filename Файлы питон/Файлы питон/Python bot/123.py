import requests
from bs4 import BeautifulSoup
LINK = 'https://wordpress.org/plugins/'

def get_html(link):
    response = requests.get(link)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article')
    return articles

def main():
    link = LINK
    print(get_data(get_html(link)))


if __name__=="__main__":
    main()