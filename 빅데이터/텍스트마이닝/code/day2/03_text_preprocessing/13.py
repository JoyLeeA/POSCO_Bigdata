from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

text = '''It is important to be immersed while you are pythoning with python. 
All pythoners have pythoned poorly at least once'''
text = text.lower()

# tokeninzer
words = word_tokenize(text)
print(words)

# stemming
porter_stemmer = PorterStemmer()
for w in words:
    print(w, porter_stemmer.stem(w))
