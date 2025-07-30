import pandas as pd
#sorting and replace the data
df_diabetes=pd.read_csv("diabetes.csv")
print(df_diabetes)
#default sorting will happen in asscending order
print(df_diabetes.sort_values("sex"))
print()
print(df_diabetes.sort_values(["age","sex"]))
print('for decending order')
print(df_diabetes.sort_values(["age","sex"],ascending=False))
print(df_diabetes)
print(df_diabetes.replace(151.0,555))
print(df_diabetes.columns)


