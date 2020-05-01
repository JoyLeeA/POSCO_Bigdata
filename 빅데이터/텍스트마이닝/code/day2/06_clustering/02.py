import pandas as pd
from konlpy.tag import Hannanum
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

hananum = Hannanum()
data = pd.read_csv("news.csv", encoding="euc-kr")
#print(data.head())

docs = []
for i in data['기사내용']:
    nouns = hananum.nouns(i)        # 기사 하나에 대해서 명사 추출
    concat_word = ' '.join(nouns)   # 리스트를 문자열로
    docs.append(concat_word)        # 모든 기사에 대해서 모우기

print(docs)
print(len(docs))
