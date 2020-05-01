import re

text = '''내가 그린 기린 그림은 잘 그린 기린 그림이고
네가 그린 기린 그림은 잘 못 그린 기린 그림이다.'''
p = re.compile(r"기린")
m = re.findall(p, text)
print(m)
