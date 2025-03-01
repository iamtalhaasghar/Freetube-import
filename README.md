# Freetube-import
Creates Freetube .db style playlist files from a list of youtube urls (.txt) or from .csv files exported from 'Google takeout'.

Run the scrip with a path to a valid list of youtube urls, or youtube's .csv playlist file. Then import the .db file into Freetube.

      python create_db.py <file>

Works without youtube api throug youtube-search. Some video names in playlists can get messed up because of this
and while the channel names are mostly ok the links to channels are broken in playlist view, the links and thumbnails will be the same though. 
These are the costs for avoiding the hassle with google's own api.

Also works atleast on piped links, probably also on lists of Invidious links and other links that follow the standard youtube url format.

###  Dependencies 
https://pypi.org/project/youtube-search/

https://pypi.org/project/tqdm/
