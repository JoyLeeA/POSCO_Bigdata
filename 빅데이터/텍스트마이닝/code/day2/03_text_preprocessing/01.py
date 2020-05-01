import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/2020/01/13/technology/oyo-hotel-india-softbank.html"
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#story > section > div:nth-of-type(1) > div > p")

text = ""
for tag in tags:
    text += tag.text

lower_text = text.lower()
print(lower_text)
