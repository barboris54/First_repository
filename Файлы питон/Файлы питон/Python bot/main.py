import telebot
import requests
from bs4 import BeautifulSoup as bs
from telebot import types


def main():
    link = 'https://ru.wordpress.org/'
    print(get_data(get_html(link)))


def get_html(link):
    request = requests.get(link)
    return request.text

def get_data(html):
    soup = bs(html,'lxml')
    h1 = soup.find('header',id="masthead").find('div').find('p').text
    return h1



if __name__ =="__main__":
    main()



bot = telebot.TeleBot('5406663508:AAF9FcahPvu31rhx79TtdE6DBmp4WaKXHZY')


