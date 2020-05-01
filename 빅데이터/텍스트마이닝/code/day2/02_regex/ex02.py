import re

text = '''
a1.xls
b1.xls
c1.xls
'''
p = re.compile(r"[ab]\d.xls")
m = p.findall(text)
print(m)