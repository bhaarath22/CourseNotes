import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.linspace(0,10,10)
y=np.cos(x)
#plt.plot(x,y,"o")
#plt.show()
#scatter function
'''plt.scatter(x,y)
plt.show()'''
#plt.scatter(x,y,marker="v")
#plt.show()
#histogram plot
'''data= nP.random.randn(1000)
plt.hist(data,color="green")
plt.show()'''
#using pandas lib

a=[2,3,4,5,6,67,7,5]
b=[43,5,6,73,6,3,63,4]
#df=pd.DataFrame({"A":a,"B":b})
#df.plot(kind="scatter",x="A",y="B")
#plt.show()
#barchart
b_x=['0-3','4-6','7-9']
b_y=[20,50,30]
#df2=pd.DataFrame({"A":b_x,"B":b_y})
#print(df2)
#df2.plot(kind="bar",x="A",y="B")

#plt.show()
#for line
l_x=['0-3','4-6','7-9']
l_y=[20,50,30]
df3=pd.DataFrame({"A":l_x,"B":l_y})
print(df3)
#df3.plot(kind="line",x="A",y="B")
#plt.show()

df3.hist()
plt.show()
