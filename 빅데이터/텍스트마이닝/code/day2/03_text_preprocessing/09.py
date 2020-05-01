# 정규 표현식을 사용하는 tokenizer
from nltk.tokenize import RegexpTokenizer

text = """
ESPRESSO
caffeinated dreams espresso blend
ESPRESSO CON PANNA
double espresso + whipped cream
ESPRESSO MACCHIATO
double espresso + milk foam -traditional
"""

tokenizer = RegexpTokenizer(r'[A-Z]+')

print(tokenizer.tokenize(text))
