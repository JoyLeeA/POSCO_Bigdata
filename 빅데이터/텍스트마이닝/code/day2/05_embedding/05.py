from sklearn.feature_extraction.text import TfidfVectorizer

text_data = [
    '나는 배가 고프다',
    '내일 점심 뭐먹지',
    '내일 공부 해야겠다.',
    '점심 먹고 공부해야지'
]

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(text_data)
print(tfidf_vectorizer.vocabulary_)

sentence = [text_data[3]]
vector = tfidf_vectorizer.transform(sentence).toarray()
print(vector)
