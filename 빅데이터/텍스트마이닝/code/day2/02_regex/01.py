text = '''
park 800905-1049118
kim 700905-1059119
'''

result = []
for line in text.split("\n"):
    for token in line.split(" "):
        if len(token) == 14 and token[:6].isdigit() and token[7:].isdigit():
            token = token[:6] + "-" + "*******"
            result.append(token)

output = "\n".join(result)
print(output)
