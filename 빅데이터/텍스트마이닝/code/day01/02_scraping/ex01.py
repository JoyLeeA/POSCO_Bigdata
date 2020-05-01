import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com"
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a")
for tag in tags:
    print(tag.text.strip())
