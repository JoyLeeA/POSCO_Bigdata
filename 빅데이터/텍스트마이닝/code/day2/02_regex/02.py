import re

text = '''
park 800905-1049118
kim 700905-1059119
'''

p = re.compile(r"(\d{6})-\d{7}")
text1 = p.sub(r"\1-*******", text)
print(text1)
