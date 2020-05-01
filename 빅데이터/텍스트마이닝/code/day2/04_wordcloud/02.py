from wordcloud import WordCloud
from nltk import FreqDist
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

text = "Boeing's troubles run deep. The 737 Max, its newest and most important jet, has been grounded since March after two deadly crashes killed 346 people."

tags = pos_tag(word_tokenize(text))
stopword = [".", ",", "'"]
result = [x[0] for x in tags if x[1][:2] == "NN" and x[0].strip() not in stopword]
print(result)

result = FreqDist(result)
print(result.most_common(5))

wc = WordCloud(width=1000, height=600, background_color="white")
fig = plt.figure(figsize=(10, 10))
plt.imshow(wc.generate_from_frequencies(result))
plt.axis("off")
plt.show()
