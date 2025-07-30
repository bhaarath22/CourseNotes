#pipeline we can perform an operation in a sequentional manner
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
data = pd.DataFrame([[1], [4], [np.NaN], [8], [11]], columns=["A"])
print(data)
# we have a missing value at index 2 ,so we need to add a value there

pipe=make_pipeline(SimpleImputer(strategy="mean"),MinMaxScaler())#imp imputation

print(pipe.named_steps['simpleimputer'])
print(pipe.named_steps['minmaxscaler'])
d1=pipe.fit_transform(data)
print("Transformed data:\n",d1)
#column transformer

column_transformer = ColumnTransformer([
    ("imp", SimpleImputer(strategy="mean"), ["A"]),
    ("scaler", MinMaxScaler(), ["A"])
])
d2= column_transformer.fit_transform(data)
print(d2)