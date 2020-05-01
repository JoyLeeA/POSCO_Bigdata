import pandas as pd
from konlpy.tag import Hannanum
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

hananum = Hannanum()
data = pd.read_csv("news.csv", encoding="euc-kr")
print(data.head())