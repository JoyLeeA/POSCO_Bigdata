import requests
import pandas as pd
from konlpy.tag import Hannanum
from wordcloud import WordCloud
import matplotlib.pyplot as plt

hananum = Hannanum()

key = "AIzaSyDooMjGlGRSg6M7Hhn_wsaCZXYpcAmlfpE"
channel = "UCtckgmUcpzqGnzcs7xEqMzQ"
video_id = "nYWpTsnJbe0"
url = "https://www.googleapis.com/youtube/v3/commentThreads?key={}&textFormat=plainText&part=snippet&videoId={}&maxResults=100".format(key, video_id)
resp = requests.get(url)
comments = resp.json()

lines = []
for comment in comments['items']:
    lines.append(comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"])

temp = []
for line in lines:
    nouns = hananum.nouns(line)
    for noun in nouns:
        if len(noun) > 1:
            temp.append(noun)

wordcloud = WordCloud(font_path="/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
                      background_color="white",
                      width=800,
                      height=800)
wordcloud = wordcloud.generate(' '.join(temp))

fig = plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
fig.savefig("peng_wordcloud.png")


