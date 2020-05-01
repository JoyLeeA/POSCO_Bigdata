from nltk import FreqDist

text = """
ESPRESSO
caffeinated dreams espresso blend
ESPRESSO CON PANNA
double espresso + whipped cream
ESPRESSO MACCHIATO
double espresso + milk foam -traditional
"""

fd = FreqDist(text.lower().split())
print(fd.most_common(5))
#fd.plot(title="Word Frequency")