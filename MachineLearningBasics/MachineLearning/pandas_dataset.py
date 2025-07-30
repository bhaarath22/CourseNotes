import pandas as pd
from sklearn.datasets import load_diabetes
data=load_diabetes()
x=data.data
y=data.target
df=pd.DataFrame(x, columns=data.feature_names)
print(df)
print('for first & last 5 entries of the dataset')
print(df.head())
print(df.tail())
print('for knowing info like missing DATA')
print(df.info())
print('for statistical data ')
print(df.describe())
print('for performing regression model we need target so to achieve that')
df["taregt"]=y
print(df.head())
#to save the data frame in  csv file for future
df.to_csv("diabetes.csv")
#if we dont need a index then do this
#df.to_csv("diabetes.csv",index=false)
#if i we want to load data from external file and create it as a data frame
df_diabetes=pd.read_csv("diabetes.csv")
print()
print(df_diabetes.head())
