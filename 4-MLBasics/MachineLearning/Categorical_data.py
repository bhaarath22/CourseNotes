from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

data={
    'color':['green','red','blue','green','green'],
'years':[0,2,3,4,2],
    'height':[2.3,43,34,55,55],
'weight':[34,45,56,65,43],
'dangerous':['yes','no','no','yes','yes']}
df=pd.DataFrame(data)
print(df)
ls= LabelEncoder()# sorting will be done, categorical data will be encoded yes=1 like this
df['dangerous']=ls.fit_transform(df['dangerous'])
print(df)

from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(dtype=int)
df[["weight"]] = oe.fit_transform(df[["weight"]])  # Make sure the column name matches your DataFrame
print()
print(df)

from sklearn.preprocessing import OneHotEncoder
ohe= OneHotEncoder(dtype=int,sparse_output=False,drop="first")
#color_encoder=ohe.fit_transform(df[["color"]])
color_encoder = ohe.fit_transform(df[["color"]])
print(color_encoder)
print(ohe.get_feature_names_out())
#LETS contaginate the feature name with original dataframe
df2=pd.DataFrame(color_encoder,columns=ohe.get_feature_names_out())
print(df2)
df=pd.concat((df,df2),axis=1)
print(df)
#no need of color column
df.drop(columns=["color"],inplace=True)
print(df)
print()
print()
#feature scalling is used when we have input data in varied scale
#minmax Scalling
#standard scalling
from sklearn.preprocessing import MinMaxScaler
mms=MinMaxScaler()
df[["years"]]=mms.fit_transform(df[["years"]])
print(df)
# maximum will be 1
print()
                                                #standard scaller mean=0,sd=1
df[["height","weight"]]=mms.fit_transform(df[["height","weight"]])
print(df)