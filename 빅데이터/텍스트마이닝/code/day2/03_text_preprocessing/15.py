from nltk import ngrams

sentence = '''Chief Justice Roberts, President Cater, President Clinton,
President Obama, fellow Americans and people of the word, thank you.
We, the citizens of America are now joined in a great national effort
to rebuild our country and restore its promise for all of our people.'''

# bi-gram
grams = ngrams(sentence.lower().split(), 2)
for gram in grams:
    print(gram)

# tri-gram
grams = ngrams(sentence.lower().split(), 3)
for gram in grams:
    print(gram)
