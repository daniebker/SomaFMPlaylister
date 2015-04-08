__author__ = 'dbaker'

from lxml import html
import requests
import argparse
from gmusicapi import Mobileclient


class Song:
    def __init__(self):
        self.name = 'song'

parser = argparse.ArgumentParser()
parser.add_argument("-u", help='Google Account Username')
parser.add_argument("-p", help='Google Account Password. If using two factor authentication you will need'
                               'an application password')
parser.add_argument("-pl", help='Playlist name')

args = parser.parse_args()

page = requests.get('http://somafm.com/defcon/songhistory.html')
tree = html.fromstring(page.text)

table = tree.xpath('//*[@id="playinc"]/table/tr')
del table[0]

song = Song()

api = Mobileclient()
logged_in = api.login(args.u, args.p)

playLists = api.get_all_user_playlist_contents()

for row in table:
    column = row.xpath('td')

    if len(column) == 5:
        song.artist = column[1].xpath('a')[0].text
        song.songName = column[2].text
        song.album = column[3].xpath('a')[0].text

        result = api.search_all_access(song.artist + " " + song.songName, 1)

        if result['song_hits']:
            for playlist in playLists:
                if playlist['name'] == args.pl:
                    songInPlaylist = False
                    for track in playlist['tracks']:
                        if track['trackId'] == result['song_hits'][0]['track']['nid']:
                            print 'playlist already contains ', song.songName
                            songInPlaylist = True

                    if not songInPlaylist:
                        print 'playlist dose not already contain ', song.songName
                        api.add_songs_to_playlist(playlist['id'],
                                                  result['song_hits'][0]['track']['nid'])











