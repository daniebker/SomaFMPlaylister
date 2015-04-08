__author__ = 'dbaker'

from lxml import html
import requests


class SomaScraper:
    root = 'http://somafm.com/'
    playlist = 'songhistory.html'

    def __init__(self):
        pass

    def get_station_history(self, station):
        page = requests.get(self.root + station + '/' + self.playlist)
        return html.fromstring(page.text)