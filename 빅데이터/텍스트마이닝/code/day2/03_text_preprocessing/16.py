from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

text = '''
Boeing's troubles run deep. The 737 MAX, its newest and most import jet, has been
grounded since March after two deadly crashes killed 346 people.
'''

tokens = word_tokenize(text)
tags = pos_tag(tokens)
print(tags)