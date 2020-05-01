from konlpy.tag import Okt

# 명사 추출
phrase = "나는 자연어 처리를 배운다"
okt = Okt()
token = okt.morphs(phrase)
print(token)

# 단어 집합 구성
word_set = {}
index = 0
for t in token:
    if t not in word_set:
        word_set[t] = index
        index += 1

def one_hot_encoding(word, word_set):
    vector = [0] * len(word_set)
    index = word_set[word]
    vector[index] = 1
    return vector

print(one_hot_encoding("자연어", word_set))