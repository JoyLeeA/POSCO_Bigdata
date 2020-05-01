import pandas as pd

# ex01
data = [100, 200, 300, 400]
s = pd.Series(data)
print(s)

# ex02
print(s.iloc[-2:])

# ex03
index = ["메로나", "누가바", "빠삐코"]
data = [500, 800, 200]
s = pd.Series(data=data, index=index)
print(s)

# ex04
s.loc["아맛나"] = 600
print(s)

# ex05
cond = s <= 500
s1 = s[cond]
print(s1)
print(s1.mean())

# ex06
data = [
    [980, 990, 920, 930],
    [200, 300, 180, 180],
    [300, 500, 300, 400]
]
columns = ["시가", "고가", "저가", "종가"]
index = ["비트코인", "리플", "이더리움"]
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
