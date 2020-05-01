import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

client_id = "kV9KBToXgWIqyXY3CGjB"
client_secret = "tcQXerzca7"

url = "https://openapi.naver.com/v1/search/book.json?query=파이썬"
headers = {
    "X-Naver-Client-id": client_id,
    "X-Naver-Client-Secret": client_secret,
}

resp = requests.get(url, headers=headers)
resp = resp.json()
data = resp['items']

# 태그 제거
def preprocessing(text):
    # HTML 태그 제거
    soup = BeautifulSoup(text, "html5lib")
    clean_text = soup.get_text()

    # 기호 제거
    p = re.compile("\W+")
    s = p.sub(" ", clean_text)
    return s

# DataFrame
df = pd.DataFrame(data=data)
df['title'] = df['title'].apply(preprocessing)
df['description'] = df['description'].apply(preprocessing)
print(df)

