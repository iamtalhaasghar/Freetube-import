# Freetube-import
Creates Freetube .db style playlist files from a list of youtube urls.

Run the scrip with a path to a valid list of youtube urls.

      python create_db.py <path_to_file>

Works without youtube api throug youtube-search. Some video names in playlists can get messed up because of this, the links and thumbnails will be the same though. Also works atleast on piped links.

###  Dependencies 
https://pypi.org/project/youtube-search/

https://pypi.org/project/tqdm/
