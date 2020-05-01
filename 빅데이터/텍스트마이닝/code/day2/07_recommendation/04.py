import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 데이터 읽은 후 20000개 샘플만 읽기
data = pd.read_csv("dataset/movies_metadata.csv", low_memory=False)
data = data.iloc[:20000]
#print(data['overview'].isnull().sum())

data['overview'] = data['overview'].fillna('')
#print(data.shape)

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
#print(tfidf_matrix.shape)

# cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
#print(cosine_sim[0][:10])

title = "The Dark Knight Rises"
title2index = pd.Series(data=data.index, index=data['title']).drop_duplicates()
index = title2index[title]

# index 번째 영화에 대한 유사도 값에 대해 [(0, 유사도), (1, 유사도) ..] 형태로 저장
sim_scores = list(enumerate(cosine_sim[index]))

# 정렬하기
sim_scores.sort(key=lambda x:x[1], reverse=True)
top10 = sim_scores[1:11]
top10_index = [x[0] for x in top10]
print(top10_index)
print(data['title'].iloc[top10_index])

