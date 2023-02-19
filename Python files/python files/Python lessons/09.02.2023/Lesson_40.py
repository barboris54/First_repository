import requests
from parsers import Paresers


def main():
    pars = Paresers('https://www.ixbt.com/live/index/news/', 'new.txt')
    pars.run()


if __name__ == '__main__':
    main()
