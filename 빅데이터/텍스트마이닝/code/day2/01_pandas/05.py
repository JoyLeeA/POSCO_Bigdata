import pandas as pd

data = {
    "제조사": ["롯데제과", "빙그레", "빙그레"],
    "가격": [2000, 1000, 1000],
    "출시년도": [1985, 1992, 1975]
}
index = ["구구콘", "메로나", "비비빅"]
df = pd.DataFrame(data=data, index=index)
print(df)