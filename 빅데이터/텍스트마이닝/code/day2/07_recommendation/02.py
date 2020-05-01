import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# 데이터 읽은 후 20000개 샘플만 읽기
data = pd.read_csv("dataset/movies_metadata.csv", low_memory=False)
data = data.iloc[:20000]
print(data['overview'].isnull().sum())

# overview가 없는 행처리
data['overview'] = data['overview'].fillna('')

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
print(tfidf_matrix.shape)
