import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import nltk

# read csv
train = pd.read_csv("./data/labeledTrainData.tsv", header=0, delimiter='\t')
test = pd.read_csv("./data/testData.tsv", header=0, delimiter='\t')

# 문장에 대해 워드 리스트로 반환
def review_to_word_list(review, remove_stopwords=False):
    # <br/> 태그 삭제
    p = re.compile(r"<\s*[Bb][Rr]\s*/>")
    review_wo_br = re.sub(p, " ", review)

    # 영문자만 남기기
    review_letters = re.sub(r"[^a-zA-Z]", " ", review_wo_br)

    # 소문자 변환 및 토근화
    lower = review_letters.lower()
    words = lower.split()

    # 불용어 제거
    if remove_stopwords:
        eng_stopwords = stopwords.words('english')
        words = [w for w in words if w not in eng_stopwords]

    # 어간추출
    stemer = SnowballStemmer('english')
    words = [stemer.stem(w) for w in words]
    return words

# 리뷰의 각 문장 단위로 워드 리스트로 구성
def review_to_sentences(review, remove_stopwords=False):
    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    sentences = tokenizer.tokenize(review.strip())

    data = []
    for sentence in sentences:
        if len(sentence) > 0:
            word_list = review_to_word_list(sentence)
            data.append(word_list)
    return data









