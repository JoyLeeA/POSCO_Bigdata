# 문장 토근화
from nltk.tokenize import sent_tokenize

text = "Boeing’s troubles run deep. The 737 Max, its newest and most important jet, has been grounded since March after two deadly crashes killed 346 people."
print(sent_tokenize(text))
