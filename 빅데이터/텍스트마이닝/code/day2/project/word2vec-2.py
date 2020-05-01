import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from konlpy.tag import Okt
from gensim.models import Word2Vec


def get_nouns(v) :
    okt = Okt()
    token = okt.pos(v, stem=True, norm=True)

    stopwords = []
#    with open("stopwords-ko.txt", encoding="utf-8") as f:
#        stopwords = f.read()
#        stopwords = result.split()

    result = ""
    for x in token:
        if x[1] == "Noun" and x[0] not in stopwords:
            result += x[0] + ' '
    return result


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
        resp = resp.json()
        data = resp['items']
        start += len(data)

        # DataFrame
        df = pd.DataFrame(data=data)
        df['title'] = df['title'].apply(preprocessing)
        df['description'] = df['description'].apply(preprocessing)
        df_list.append(df)

        # break
        if len(data) != 100:
            break

    return pd.concat(df_list)

if __name__ == "__main__":
#    df = request_book_by_query("파이썬")
    target = df['title'] + ' ' + df['description']
    target = target.apply(get_nouns)
    target = '(저)' + df['author'] + ' ' + target
    target = target.str.split()

    # Training
    model = Word2Vec(target.to_list(), size=300, window=10, min_count=1)
    model.init_sims(replace=True)

    # Test
    result = model.wv.most_similar("(저)조대표", topn=1000)

    p = re.compile("\(저\)\w+")
    for x in result:
        m = p.findall(x[0])
        if len(m) > 0 :
            print(m[0])
