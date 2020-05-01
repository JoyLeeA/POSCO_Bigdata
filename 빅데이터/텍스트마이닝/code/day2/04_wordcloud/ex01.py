import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 파일 읽기
f = open("트럼프취임연설문.txt", "r")
lines = f.readlines()[0]
f.close()

# 전처리 및 토근화
text = lines.lower()    # 소문자
tokenizer = RegexpTokenizer("\w+")
tokens = tokenizer.tokenize(text)

# 불용어 제거
eng_stopwords = stopwords.words("english")
stopwords_removed_tokens = [w for w in tokens if w not in eng_stopwords and len(w) > 1]

# 빈도수 확인
s = pd.Series(stopwords_removed_tokens)
print(s.value_counts().head(10))

# wordcloud
wordcloud = WordCloud(background_color="white",
                      width=800,
                      height=800)
wordcloud = wordcloud.generate(' '.join(stopwords_removed_tokens))

fig = plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
fig.savefig("trump.png")
