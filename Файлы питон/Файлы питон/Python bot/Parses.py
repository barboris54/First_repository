import csv

import requests
from bs4 import BeautifulSoup as bs
LINK = 'https://wordpress.org/plugins/'

def get_html(link):
    response = requests.get(link)
    return response.text

def refinde(str):
    s = str.split(' ')[0]
    return s.replace(',', '')

def write_csv(data):
    with open('listplugins3.csv','a') as f:
        recorder = csv.writer(f)

        recorder.writerow((data['h3'],
                           data['link'],
                           data['rating']))


def get_data(html):
    soup = bs(html, 'lxml')
    articles = soup.find_all('article')
    for article in articles:
        h3 = article.find('h3',class_='entry-title').text
        link = article.find('h3',class_='entry-title').find('a').get('href')
        rating = article.find('div', class_='plugin-rating').find('span',class_='rating-count').find('a').text
        print(h3,link,refinde(rating))

        data ={'h3':h3,
               'link':link,
                'rating':rating}
        write_csv(data)

def main():
    link = LINK
    print(get_data(get_html(link)))


if __name__ =='__main__':
   main()

