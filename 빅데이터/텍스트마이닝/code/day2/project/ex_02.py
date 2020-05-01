import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


def preprocessing(text):
    # HTML 태그 제거
    soup = BeautifulSoup(text, "html5lib")
    clean_text = soup.get_text()

    # 기호 제거
    p = re.compile("\W+")
    s = p.sub(" ", clean_text)
    return s


def request_book_by_query(query="파이썬"):
    client_id = "kV9KBToXgWIqyXY3CGjB"
    client_secret = "tcQXerzca7"

    url = "https://openapi.naver.com/v1/search/book.json"
    headers = {
        "X-Naver-Client-id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }

    start = 1
    df_list = []
    while start <= 1000:
        params = {
            "query": query,
            "start": start,
            "display": 100
        }

        resp = requests.get(url, params=params, headers=headers)
        print(resp.url)
        resp = resp.json()
        data = resp['items']
        start += len(data)

        # DataFrame
        df = pd.DataFrame(data=data)
        print(df)
        df['title'] = df['title'].apply(preprocessing)
        df['description'] = df['description'].apply(preprocessing)
        df_list.append(df)

        # break
        if len(data) != 100:
            break

    return pd.concat(df_list)

if __name__ == "__main__":
    df = request_book_by_query("파이썬")
    print(df)

