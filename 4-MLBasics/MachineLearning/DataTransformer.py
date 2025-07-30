import pandas as pd
from sklearn.preprocessing import StandardScaler
x=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print(x)
print(x.describe())
ss=StandardScaler()
ss.fit(x)
print("mean")
print(ss.mean_)
print(ss.var_)
print()
#perform transform on x to get mean-0,std 1
x_scalled=ss.transform(x)
print(x_scalled)
print(pd.DataFrame(x_scalled).describe())
#used in linear regression model ,when multiple columns and each columns as there own set of scales if we apply direct ML we cant trust it so we perform Standard scaller in linear regression