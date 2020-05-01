import pandas as pd
from konlpy.tag import Hannanum
from wordcloud import WordCloud
import matplotlib.pyplot as plt

hannanum = Hannanum()

f = open("문재인대통령취임사.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

temp = []
for line in lines:                              # 각 라인에 대해
    nouns = hannanum.nouns(line)                # 각 라인에서 명사 추출
    for noun in nouns:                          # 추출된 명사에 대해
        if len(noun) > 1:
            temp.append(noun)

s = pd.Series(temp)
s1 = s.value_counts()
print(s1.head(10))

wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white",
                      width=800,
                      height=800)
wordcloud = wordcloud.generate(' '.join(temp))

fig = plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
fig.savefig("wordcloud.png")
