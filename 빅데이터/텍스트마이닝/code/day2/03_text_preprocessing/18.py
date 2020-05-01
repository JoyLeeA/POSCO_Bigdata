from konlpy.tag import Hannanum

phrase = "친척들이 모인 이번 설에서는 단연 '취업'이 화제에 올랐다."
hannanum = Hannanum()

print(hannanum.morphs(phrase))
print(hannanum.nouns(phrase))
print(hannanum.pos(phrase))