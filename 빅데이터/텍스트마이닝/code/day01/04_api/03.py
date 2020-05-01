import requests
import pandas as pd

key = "AIzaSyCtdd_n7FsI6aTV_speDI8RbqE_HSN3Zk4"
channel = "UCtckgmUcpzqGnzcs7xEqMzQ"
video_id = "nYWpTsnJbe0"
url = "https://www.googleapis.com/youtube/v3/commentThreads?key={}&textFormat=plainText&part=snippet&videoId={}&maxResults=100".format(key, video_id)

resp = requests.get(url)
comments = resp.json()
for comment in comments['items']:
    print(comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
