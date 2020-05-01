from konlpy.tag import Okt
from gensim.models import Word2Vec

data = ["철수는 학교에서 자연어를 공부한다",
              "영철이는 학교에서 영어를 공부한다",
              "영희는 집에서 영어를 공부한다",
              "아이유는 집에서 자연어를 공부한다",]

okt = Okt()
result = []
for v in data :
    token = okt.pos(v, stem=True, norm=True)
    result.append([x[0] for x in token if x[1] == "Noun"])

model = Word2Vec(result, size=5, window=2, min_count=2, sg=0)
value = model.wv.most_similar("자연어")
print(value)
#print(model.wv['자연어'])