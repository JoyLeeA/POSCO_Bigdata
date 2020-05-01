from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import requests
from bs4 import BeautifulSoup

url = "https://www.whitehouse.gov/briefings-statements/the-inaugural-address/"
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, 'html5lib')
tags = soup.select("#main-content > div.page-content > div > div > p")

text = ""
for tag in tags:
    text += tag.text + " "

lower_text = text.lower()
print(lower_text)

tokenizer = RegexpTokenizer(r"\w+")
result = [x for x in tokenizer.tokenize(lower_text) if x not in stopwords.words('english')]

fd_names = FreqDist(result)
print(fd_names.most_common(5))
