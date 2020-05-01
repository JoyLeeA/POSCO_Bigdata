import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/board.nhn?code=005490"
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#content > div.section.inner_sub > table.type2 > tbody > tr > td.title > a")

for tag in tags[:5]:
    print(tag['title'].strip())
