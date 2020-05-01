import re

text = '''
Brayden Jo 010-8212-1212 brayden.jo@outlook.com
Lukas Yoo 010-8767-1212 lukas.yoo@gmail.com
'''

p = re.compile(r"\d")
m = p.findall(text)
print(m)
