import requests
import pandas as pd

key = "AIzaSyCtdd_n7FsI6aTV_speDI8RbqE_HSN3Zk4"
channel = "UCtckgmUcpzqGnzcs7xEqMzQ"
url = "https://www.googleapis.com/youtube/v3/search?channelId={}&part=snippet&key={}".format(channel, key)
resp = requests.get(url)
videos = resp.json()

video_data = []
for video in videos["items"]:
    publishedAt = video["snippet"]["publishedAt"]
    title = video["snippet"]["title"]
    description = video["snippet"]["description"]
    thumbnail = video["snippet"]["thumbnails"]["default"]["url"]
    video_data.append([publishedAt, title, description, thumbnail])

columns = ["publishedAt", "title", "description", "thumbnail"]
df = pd.DataFrame(data=video_data, columns=columns)
df.to_csv("peng.csv", encoding="euc-kr")
