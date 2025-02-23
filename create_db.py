import uuid
import time
from sys import argv
from youtube_search import YoutubeSearch
import json
from tqdm import tqdm

def YT_authordata(yt_id):

    results = YoutubeSearch('https://www.youtube.com/watch?v='+yt_id, max_results=1).to_dict()
    return results
if 2>len(argv):
    print("You must include a path to a valid .txt file")
    exit(1)
inputfile_name = argv[1]
filenamesplit=inputfile_name.split(".")
playlistname=filenamesplit[0]
outputfile=open(playlistname+".db","w")
playlist_UUID=uuid.uuid4()
current_time_ms = int(time.time() * 1000)

inputfile=open(inputfile_name,"r")
Videos=inputfile.readlines()
Video_IDs=[]
for i in Videos:
    id=i.split("?v=")
    id=id[1].rstrip()
    Video_IDs.append(id)

inputfile.close()
print(f"Reading file {inputfile_name}, the to be converted playlistfile has {len(Video_IDs)} entries")
print(f"writing to file {playlistname}.db")
playlist_dict=dict(
    playlistName=playlistname,
    videos=[],
    _id="ft-playlist--"+str(playlist_UUID),
    createdAt=current_time_ms,
    lastUpdatedAt=current_time_ms
)

counter =0
for i in tqdm(Video_IDs):
#for i in Video_IDs:
    video_UUID=uuid.uuid4()
    current_time_ms = int(time.time()*1000)
    videoinfo=YT_authordata(i)
    if len(videoinfo)==0:
        continue
    video_dict=dict(
        videoId=i,
        title=videoinfo[0]['title'],
        author=videoinfo[0]['channel'],
        authorId="UC2hkwpSfrl6iniQNbwFXMog",
        published="",
        lengthSeconds="0:00",
        timeAdded=current_time_ms,
        type="video",
        playlistItemId=str(video_UUID)


    )
    playlist_dict["videos"].append(video_dict)
outputfile.write(json.dumps(playlist_dict,separators=(',', ':'))+"\n")
outputfile.close()
print(f"Task failed successfully! File {playlistname}.db written in file")
