import time

import requests
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, url: str):
        self.url = url
        self.current_time = time.time()

    @property
    def website(self):
        r = requests.get(self.url)
        return r.text

    @classmethod
    def refined(cls, text: str):
        return text.split()[0]

    def get_data(self):
        soup = BeautifulSoup(self.website, 'lxml')
        popular = soup.find_all('section', class_='plugin-section')[1]
        plugins = popular.find_all('article')

        for plugin in plugins:
            name = plugin.find('h3').text
            url = plugin.find('h3').find('a').get('href')

            rating = plugin.find('div', class_='plugin-rating').find('div', class_='wporg-ratings').attrs
            locator = plugin.find('div', class_='entry').find('span', class_='rating-count')
            locator_text = locator.find('a').text

            vote_counts = self.refined(locator_text)

            print(f"Name: '{name}'\nLink: {url}\nRating: {rating['aria-label']}\nNumber of voters: {vote_counts}")

        return plugins


if __name__ == '__main__':
    parser = HtmlParser('https://wordpress.org/plugins/')
    print(parser.current_time)
