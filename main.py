import requests
from bs4 import BeautifulSoup
import lxml
import csv


def get_html(url):
    r = requests.get(url=url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text.strip()
    return h1

def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()