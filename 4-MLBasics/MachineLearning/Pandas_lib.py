#pandas is open source python library ,used for data analysis and machine learning
#build upon numpy libraray.//dataramling
import pandas as pd
# pandas objects .referring rows and columns with labels instead of index values in numpy ,padaseries and pandadata
data=pd.Series([1,2,3,4,5,6])
print(data)
print(type(data))
print(data.values)
print(data.index)
print(data[1])
print()
dAta=pd.Series(data=[10,24,34,45], index=list("abcd"),dtype="float",name="example_Series")
print(dAta)
print(dAta.name)
print('conversion of python list into pandas series')
tour_place={"hyderabad":2323,"mumbai":3232,"delhi":4343,"tamilNadu":5454}
print(tour_place)
print('after python dictonary to pandas series')
pop_series=pd.Series(tour_place)
print(pop_series)
print('pandasDataframe')
cost_ofLiving={"hyderabad":233,"mumbai":322,"delhi":443,"tamilNadu":334}
pop_series2=pd.Series(cost_ofLiving)
print(pop_series2)
df=pd.DataFrame({"city":pop_series,"cost_ofliving":cost_ofLiving})
print(df)
#pandas dataframe is collection od pandas seriesor dictonaries .rows and columns
print(df.columns)
print(df.index)
print()
print(df.city)
print(type(df["city"]))
print("array")
import numpy as np
np.random.seed(0)
array=np.random.randint(4,400,size=(4,5))
print(array)
df2=pd.DataFrame(array,index=list("abcd"),columns=("col1","col2","col3","col4","col5"))
print(df2)
print(df2.values)
print(df2.columns)
print(df2.index)