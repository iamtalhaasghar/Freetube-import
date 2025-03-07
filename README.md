# Freetube-import
Creates Freetube .db style playlist files from a list of youtube urls (.txt) or from .csv files exported from 'Google takeout'.

Run the scrip with a path to a valid list of youtube urls, or youtube's .csv playlist file. Then import the .db file into Freetube.

      python create_db.py <file>

help

      usage: create_db.py [-h] [-l] filepath

      Import youtube playlists

      positional arguments:
        filepath          path to a valid .txt or .csv playlist file

      optional arguments:
        -h, --help        show this help message and exit
        -l, --log-errors  Also lists the videos that failed the metadata fetch

Works without YouTube api through YouTube-search. 

While the script should work perfectly for 95% of the videos, minority of video and channel names in the playlist view can get messed up because of this, due to incorrect metadata fetch. Even while of the channel names are ok, The links to channel profile's are all broken in playlist view, since the fetching of proper channel-id's is not possible to get through this method. The video links themselves and their respective thumbnails should be the same though in all circumstances, and all the proper names and data is viewing correctly once the video is opened. Removing and re-adding the affected video from the playlist within Freetube should fix these flaws. 
These are the costs for avoiding the hassle with google's own api.

Also works atleast on piped links, probably also on lists of Invidious links and other links that follow the standard youtube url format.

###  Dependencies 

       pip install youtube-search
https://pypi.org/project/youtube-search/

      pip install tqdm
https://pypi.org/project/tqdm/
