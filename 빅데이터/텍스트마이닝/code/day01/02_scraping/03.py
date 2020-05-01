import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005490"
resp = requests.get(url)
html = resp.text



soup = BeautifulSoup(html, "html5lib")
per_tag = soup.select("#_per")
pbr_tag = soup.select("#_pbr")
print(per_tag[0].text)
print(pbr_tag[0].text)
