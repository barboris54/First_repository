import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.anekdot.ru/last/good/'
response = requests.get(url).text




def parsing_anekdots(text):
    soup = BeautifulSoup(text, 'html.parser')
    anekdot = soup.find_all('div', class_='text')
    for i in anekdot:
        anekdots = []
        anekdots.append(i.text)
        print(anekdots)

        with open('anekdots.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\r', delimiter=';')
            writer.writerow(anekdots)





parsing_anekdots(response)