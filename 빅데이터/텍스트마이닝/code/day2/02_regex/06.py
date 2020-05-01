import re

text = "010-1234-5678"
p = re.compile(r"-")
m = re.sub(p, "/", text)
print(m)