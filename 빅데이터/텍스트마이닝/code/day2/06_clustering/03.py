import pandas as pd
from konlpy.tag import Hannanum
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

hananum = Hannanum()
data = pd.read_csv("news.csv", encoding="euc-kr")
#print(data.head())

docs = []
for i in data['기사내용']:
    nouns = hananum.nouns(i)
    concat_word = ' '.join(nouns)
    docs.append(concat_word)

#print(docs)
#print(len(docs))
# counter vectorizer
vectorizer = CountVectorizer()
vec = vectorizer.fit_transform(docs)
print(vec.shape)
#print(vectorizer.get_feature_names())
#print(len(vectorizer.get_feature_names()))

# 4. Kmeans
df = pd.DataFrame(vec.toarray(), columns=vectorizer.get_feature_names())
kmeans = KMeans(n_clusters=3).fit(df)
print(kmeans.labels_)

