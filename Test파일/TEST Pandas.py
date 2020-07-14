import csv
import pandas as pd
import numpy as np


my_data = np.array([100,200,300,400])
series1 = pd.Series(data=my_data, index=['a', 'b', 'c', 'd'])

# # print(series1)
# data = {'name' : ['lion', 'king'], 'age' : [10,20]}
# af = pd.DataFrame(data)
# print(pd.DataFrame(af))
# print(af.shape)
# print(len(af.index))

# bf = pd.DataFrame({"A" : [1,4,7], "B" : [2,5,8], "C" : [3,6,9]})
# print(bf)
# print("\n")
# print(bf['A'])
# print("\n")
# print(bf.loc[:, 'A'])

# print("\n")
# print(bf.loc[0]['A'])



# df = pd.read_csv('data_iris.csv')
# df.describe()


cf = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])
cf['d'] = pd.Series(['5','6','7'], index = cf.index)


print(cf)