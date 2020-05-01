import re

text = '''
Brayden Jo 010-8212-1212 Brayden.jo@outlook.com
Lukas Yoo 01087671212 Lukas.yoo@gmail.com
'''

p = re.compile(r"\d+-?\d+-?\d+")
m = p.findall(text)

print(m)