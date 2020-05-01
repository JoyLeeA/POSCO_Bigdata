import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/moonriver365"
resp = requests.get(url)
html = resp.text

#f = open("temp.html", "w", encoding="utf-8")
#f.write(html)
#f.close()

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#stream-items-id li.js-stream-item.stream-item.stream-item  div.content div.js-tweet-text-container > p")
for tag in tags[:3]:
    print(tag.text)
