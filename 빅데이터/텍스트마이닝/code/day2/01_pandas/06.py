# 데이터 프레임 생성 (로우 단위로 데이터 표현)
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