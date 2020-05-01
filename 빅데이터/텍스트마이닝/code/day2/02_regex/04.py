import re

text = "불가능을 가능하게!"
p = re.compile(r"가능")
m = re.search(p, text)
print(m)
if m:
    print(m.group())
