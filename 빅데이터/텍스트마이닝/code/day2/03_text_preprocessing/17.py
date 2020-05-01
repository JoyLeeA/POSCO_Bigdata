from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

text = "Boeing's troubles run deep. The 737 Max, its newest and most important jet, has been grounded since March after two deadly crashes killed 346 people."
tokens = word_tokenize(text)
tags = pos_tag(tokens)
result = [x[0] for x in tags if x[1][:2] == "NN"]
print(result)
