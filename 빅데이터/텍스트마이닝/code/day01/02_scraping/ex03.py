import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=159866"
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#reviewTab > div > div > ul > li > p > a")

for tag in tags[:4]:
    print(tag.text)
