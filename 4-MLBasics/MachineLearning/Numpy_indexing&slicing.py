#boolean,int,complex,float,string=object data types we can arrange with numpy array
import numpy as np
x=np.random.randint(10,45,size=(4,5))
print(x)
print(x[2,1])
print(x[2])
print(x[-2])
print(x[-1,-2])
print(x[1:3])
print(x[1:3,1:3])
print()
y=np.random.randint(0,1000,size=(7,7))
print(y)
print(y[2:6,2])
#start end stepsize
print(y[2:3:4,3:4:5])