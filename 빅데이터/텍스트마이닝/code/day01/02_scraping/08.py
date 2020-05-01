import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("div div div div ul li a span")
print(tags)

