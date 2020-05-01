from konlpy.tag import Okt

document = "봄과 함께 찾아온 따뜻한 신제품 소식"
okt = Okt()

words = okt.pos(document, stem=True)

clean_words = []
for word in words:
    if word[1] in ['Noun', 'Verb', 'Adjective']:
        clean_words.append(word[0])

print(clean_words)