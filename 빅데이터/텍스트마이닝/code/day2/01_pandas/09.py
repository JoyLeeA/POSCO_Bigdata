# 데이터 프레임 인덱싱
import pandas as pd

data = [
    ["롯데제과", 2000, 1985],
    ["빙그레", 1000, 1992],
    ["빙그레", 1000, 1975]
]
columns = ["제조사", "가격", "출시년도"]
index = ["구구콘", "메로나", "비비빅"]
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)

# 인덱싱
print(df.iloc[[0, 1], [0, 1]])
print(df.loc[["구구콘", "메로나"], ["제조사", "가격"]])
