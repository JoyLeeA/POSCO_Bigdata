from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer

# word tokenizer
text = "@Jason, Let's finish #projectA quickly."
print(word_tokenize(text))

# tweeter tokenizer
tknzr = TweetTokenizer()
print(tknzr.tokenize(text))

