from sklearn.feature_extraction.text import CountVectorizer

text_data = [
    '나는 배가 고프다',
    '내일 점심 뭐먹지',
    '내일 공부 해야겠다.',
    '점심 먹고 공부해야지'
]

# 단어 사전 구성
count_vectorizer = CountVectorizer()     # 객체 생성
count_vectorizer.fit(text_data)          # 단어 목록 생성
print(count_vectorizer.vocabulary_)
print(len(count_vectorizer.vocabulary_))

# 문장을 벡터화
sentence = [text_data[0]]       # 첫 번째 문장
vector = count_vectorizer.transform(sentence).toarray()          # transform
print(vector)