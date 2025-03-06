import uuid
import time
from sys import argv
from pathlib import Path
from youtube_search import YoutubeSearch
import json
from tqdm import tqdm

def YT_authordata(yt_id):
    results = YoutubeSearch('https://www.youtube.com/watch?v='+yt_id, max_results=1).to_dict()
    return results

def process_txt(path):
    with open(path, "r") as inputfile:
        Videos=inputfile.readlines()
        Video_IDs=[]
        for i in Videos:
            id=i.split("?v=")
            try:
                id=id[1].rstrip()
                Video_IDs.append(id)
            except IndexError:
                pass
    return Video_IDs

def process_csv(path):
    with open(path, "r") as inputfile:
        Videos=inputfile.readlines()
        Video_IDs=[]
        data_start=False
        for i in Videos:
            if i.split(",")[0]=="Video ID":
                data_start=True
                continue
            if data_start:
                Video_IDs.append(i.split(",")[0])
    return Video_IDs

if 2>len(argv):
    print("You must include a path to a valid .txt file or youtube .csv playlistfile")
    exit(1)
inputfile_name = argv[1]
playlistname=str(Path(inputfile_name).name)
playlistformat=playlistname.split(".")[1]
playlistname=playlistname.split(".")[0]
playlist_UUID=uuid.uuid4()
current_time_ms = int(time.time() * 1000)
Video_IDs=[]
if playlistformat=="txt":
    Video_IDs=process_txt(inputfile_name)
elif playlistformat=="csv":
    Video_IDs=process_csv(inputfile_name)
else:
    print(f"{playlistformat} is invalid file format.")
    exit(1)

outputfile=open(playlistname+".db","w")
print(f"Reading file {inputfile_name}, the playlistfile has {len(Video_IDs)} entries")
print(f"writing to file {playlistname}.db")
playlist_dict=dict(
    playlistName=playlistname,
    videos=[],
    _id="ft-playlist--"+str(playlist_UUID),
    createdAt=current_time_ms,
    lastUpdatedAt=current_time_ms
)
counter=0
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
    counter+=1
outputfile.write(json.dumps(playlist_dict,separators=(',', ':'))+"\n")
outputfile.close()
print(f"Task failed successfully! {playlistname}.db written, with {counter} entries")
