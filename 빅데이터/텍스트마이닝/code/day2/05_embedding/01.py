from konlpy.tag import Okt

phrase = "나는 자연어 처리를 배운다"
okt = Okt()
token = okt.morphs(phrase)
print(token)

word_set = {}
index = 0
for t in token:
    if t not in word_set:
        word_set[t] = index
        index += 1

print(word_set)