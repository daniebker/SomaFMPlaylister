__author__ = 'dbaker'

from gmusicapi import Mobileclient


class GoogleMusicApi:

    api = Mobileclient()

    def __init__(self):
        pass

    def login(self, user, password):
        logged_in = self.api.login(user, password)
        if not logged_in:
            raise Exception("Could not log in")

    def get_playlist(self, name):
        playlists = self.api.get_all_user_playlist_contents()
        playlist = next(p for p in playlists if p['name'] == name)

        if not playlist:
            raise Exception("Cannot find playlist")

        return playlist

    def search(self, sog):
