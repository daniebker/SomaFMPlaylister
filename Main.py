__author__ = 'dbaker'

import argparse

from gmusicapi import Mobileclient
from Scrapers import SomaScraper
from MusicData import Song

parser = argparse.ArgumentParser()
parser.add_argument("-u", help='Google Account Username', required=True)
parser.add_argument("-p", help='Google Account Password. If using two factor authentication you will need'
                               'an application password', required=True)
parser.add_argument("-pl", help='Playlist name', required=True)
parser.add_argument("-li", type=int, help='Limits the number of tracks to look back. To add now playing set this to 1')
args = parser.parse_args()

scraper = SomaScraper()
tree = scraper.get_station_history('defcon')

table = tree.xpath('//*[@id="playinc"]/table/tr')

# remove the table header.
del table[0]

song = Song()

api = Mobileclient()
logged_in = api.login(args.u, args.p)

if args.li:
    count = min(len(table), args.li)
else:
    count = len(table)

if logged_in:
    playLists = api.get_all_user_playlist_contents()
    playlist = next(p for p in playLists if p['name'] == args.pl)

    for i in range(0, count):
        column = table[i].xpath('td')

        """SomaFM prints breaks and in the schedule so we only want rows in the
            table that are a track"""
        if len(column) == 5:
            song.artist = column[1].xpath('a')[0].text
            song.songName = column[2].text
            song.album = column[3].xpath('a')[0].text

            result = api.search_all_access(song.artist + " " + song.songName, 1)

            if result['song_hits']:
                songInPlaylist = False
                for track in playlist['tracks']:
                    if track['trackId'] == result['song_hits'][0]['track']['nid']:
                        print 'playlist already contains ', song.songName
                        songInPlaylist = True

                if not songInPlaylist:
                    print 'playlist dose not already contain ', song.songName
                    api.add_songs_to_playlist(playlist['id'],
                                              result['song_hits'][0]['track']['nid'])