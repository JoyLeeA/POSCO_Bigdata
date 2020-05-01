import re

text = '''
Send personal email to ben@forta.com. For questions
about a book use support@forta.com. Feel free to send
unsolicited email to spam@forta.com (wouldn't it be
nice if it were that simple, huh?).
'''

p = re.compile(r"\w+@\w+.\w+")
m = p.findall(text)
print(m)