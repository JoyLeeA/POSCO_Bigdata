from konlpy.tag import Okt
from konlpy.tag import Komoran
import re

# 분석할 텍스트 읽어오기
with open('news.txt', 'r', encoding='utf8') as f:
    content = f.read()

# 불필요한 심볼 없애기
p = re.compile("[\Wa-zA-Z0-9_]+")
content = re.sub(p, " ", content)

# 형태소 분석 및 단어 추출
okt = Okt()
okt_morphs = okt.pos(content)
print(okt_morphs)

# 명사, 조사, 네이밍 표현을 다시 변경
komoran = Komoran()
komoran_morphs = komoran.pos(content)
print(komoran_morphs)

# 명사만 추출하기
words = []
for word, pos in okt_morphs:
    if pos == 'Noun':
        words.append(word)
print(words)