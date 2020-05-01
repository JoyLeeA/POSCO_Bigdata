import pandas as pd

train = pd.read_csv("./data/labeledTrainData.tsv", header=0, delimiter='\t')
test = pd.read_csv("./data/testData.tsv", header=0, delimiter='\t')

print(train.shape)
print(test.shape)
print(train.head())
print(test.head())
