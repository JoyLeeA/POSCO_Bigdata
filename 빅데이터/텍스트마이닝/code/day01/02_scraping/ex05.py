import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005490"
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, "html5lib")
per_tags = soup.select("#_per")
pbr_tags = soup.select("#_pbr")
print(per_tags[0].text)
print(pbr_tags[0].text)
