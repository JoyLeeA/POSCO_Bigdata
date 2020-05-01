from pandas import Series

data = [1000, 2000, 3000]
index = ['메로나', '구구콘', '하겐다즈']
s = Series(data=data, index=index)

print(s.iloc[0])
print(s.loc['메로나'])
print(s['메로나'])