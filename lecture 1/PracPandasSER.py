# PANDAS works with null data
import pandas as pd

# SERIES:
# making series so we can see the data like we do in excel

x=[1,2,8,3,4,9]
v1 = pd.Series(x)
print(v1)

# we can change the indexes and the data type as well
v1 = pd.Series(x,index=["a","b","c","d","e","f"], dtype="float")
print(v1)

# specifies the missing values
s1=pd.Series(2,index=[1,2,3,4])
s2=pd.Series(2,index=[1,2,3])
print(s1+s2)
# since there is no number at index 4 in s2 so the output for index 4 would be NaN
