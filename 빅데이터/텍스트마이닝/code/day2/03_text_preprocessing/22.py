import konlpy.tag
import re
from collections import Counter

# 분석할 텍스트 읽어오기
with open('news.txt', 'r', encoding='utf8') as f:
    content = f.read()

# 불필요한 심볼 없애기
p = re.compile("[\Wa-zA-Z0-9_]+")
content = re.sub(p, " ", content)

# 형태소 분석 및 단어 추출
okt = konlpy.tag.Okt()
okt_morphs = okt.pos(content)
print(okt_morphs)

# 명사, 조사, 네이밍 표현을 다시 변경
komoran = konlpy.tag.Komoran()
komoran_morphs = komoran.pos(content)
print(komoran_morphs)

# 명사만 추출하기
words = []
for word, pos in okt_morphs:
    if pos == 'Noun':
        words.append(word)
print(words)

# 불용어 제거
stopwords = ['출처', '뉴스', '원본', '링크']
result = [x for x in words if x not in stopwords and len(x) > 1]
print(result)

## 빈도 분석, 각 단어들이 몇 번 사용되었는지 분석
c = Counter(result)
print(c.most_common(10))
