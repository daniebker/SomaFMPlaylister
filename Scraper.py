__author__ = 'dbaker'

from lxml import html
import requests


def process_row(row):
    for cell in row.xpath('./td'):
        print cell.text_content()
        yield cell.text_content()


page = requests.get('http://somafm.com/defcon/songhistory.html')
tree = html.fromstring(page.text)

table = tree.xpath('//*[@id="playinc"]/table/tr')

songs = []

for row in table:
    column = row.xpath('td')
    for c in column:
        if c.text is None:
            link = c.xpath('a')
            try:
                print link[0].text
            except IndexError:
                print 'nothing'
        else:
            print c.text


class Song:
    name
    artist

    def __init__(self):

    d
