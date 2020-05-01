import re

p = re.compile("[0-9]+")    # 숫자 하나  이상
print(p.sub("", "서울 집값이 평균 30% 상승했습니다."))

p = re.compile("\W+")              # \w 의 반대
print(p.sub(" ", "★파이썬 좋아요. 신나요~"))
