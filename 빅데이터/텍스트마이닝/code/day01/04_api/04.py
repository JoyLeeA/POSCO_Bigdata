import requests
import pandas as pd
import time

key = "AIzaSyCtdd_n7FsI6aTV_speDI8RbqE_HSN3Zk4"
channel = "UCtckgmUcpzqGnzcs7xEqMzQ"
video_id = "nYWpTsnJbe0"
url = "https://www.googleapis.com/youtube/v3/commentThreads?key={}&textFormat=plainText&part=snippet&videoId={}&maxResults=100".format(key, video_id)

resp = requests.get(url)
comments = resp.json()

while True:
    if comments.get("nextPageToken") is not None:
        next_page_token = comments.get('nextPageToken')
    else:
        break

    # 100개 출력
    for comment in comments['items']:
        print(comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"])

    url2 = url + "&pageToken=" + next_page_token
    resp = requests.get(url2)
    comments = resp.json()

    time.sleep(1)
