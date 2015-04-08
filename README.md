# SomaFMPlaylister
Takes recently played tracks on a SomaFM station and adds them to a Google Music All Access playlist

# Usage

python main.py -u [EMAIL] -p [PASSWORD] -pl "SomaFm - DefCon" -li 5

* -u: Your Google Email Address
* -p: Your Google Password. If you're using two factor authentication then you will need to produce an Application Specific Password.
* -pl: The name of the playlist to add the songs to. This must be existing.
* -li: Optional. Limits to the last x entries where x is the number of entries you want to look back. This currently doesn't take into account entries in the history that are not songs.