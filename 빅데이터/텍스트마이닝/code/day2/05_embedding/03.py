from konlpy.tag import Okt
import re

# 전처리
text1 = "정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다."
text1 = re.sub(r"\.", "", text1)

# 형태소 분리
okt = Okt()
token = okt.morphs(text1)

# BoW 구성
bow = {}
index = 0
for t in token:
    if t not in bow:
        bow[t] = index
        index += 1
print(bow)

# 벡터화
vec = []
for w, i in bow.items():
    count = token.count(w)
    vec.append(count)

print(vec)
