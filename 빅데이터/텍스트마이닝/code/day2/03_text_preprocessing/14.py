from konlpy.tag import Okt

okt = Okt()
text = "한글 자연어 처리는 재밌다. 이제부터 열심히 해야지."
text = "한글 자연어 처리는 재밌다. 이제부터 열심히 해야겠누."
text = "한글 자연어 처리는 재밌다. 이제부터 열심히 조져야지 ."
text = "목이 너무 아프다. 목을 삼백육십도 돌려서 근육을 전부 없애버리고 싶"

print(okt.morphs(text))
print(okt.morphs(text, stem=True))