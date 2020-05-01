import re

text = "불가능을 가능하게!"
p = re.compile(r"가능")
m = re.findall(p, text)
print(m)