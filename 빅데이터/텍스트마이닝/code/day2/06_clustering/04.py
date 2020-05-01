import pandas as pd
from konlpy.tag import Hannanum
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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

# 4. Kmeans
df = pd.DataFrame(vec.toarray(), columns=vectorizer.get_feature_names())
kmeans = KMeans(n_clusters=3).fit(df)
print(kmeans.labels_)

# 5. PCA 차원 축소
pca = PCA(n_components=2)
principle_comp = pca.fit_transform(df)
principle_df = pd.DataFrame(data=principle_comp,
                            index=data['검색어'],
                            columns=['comp1', 'comp2'])

plt.scatter(principle_df.iloc[kmeans.labels_ == 0, 0],
            principle_df.iloc[kmeans.labels_ == 0, 1],
            s=10, c='red', label='cluster1')
plt.legend()
plt.show()



