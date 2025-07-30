import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)

'''plt.plot(x,np.sin(x),color="red")
plt.plot(x,np.sin(x+1),color="g")
plt.plot(x,np.sin(x+2),color="0.8")#grey scale value
plt.plot(x,np.sin(x+3),color="#FFDD44")#xcode
plt.show()'''

#linestyle
'''plt.plot(x,np.sin(x),color="red",linestyle="solid")
plt.plot(x,np.sin(x+1),color="g",linestyle="dashed")
plt.plot(x,np.sin(x+2),color="0.8",linestyle="dashdot")#grey scale value
plt.plot(x,np.sin(x+3),color="#FFDD44",linestyle="dotted")#xcode
plt.show()'''

'''plt.plot(x,np.sin(x),color="red",linestyle="-")
plt.plot(x,np.sin(x+1),color="g",linestyle="--")
plt.plot(x,np.sin(x+2),color="0.8",linestyle="-.")#grey scale value
plt.plot(x,np.sin(x+3),color="#FFDD44",linestyle=":")#xcode
plt.show()'''

'''plt.plot(x,np.sin(x),"-g")
plt.plot(x,np.sin(x+1),"--c")
plt.plot(x,np.sin(x+2),"-.k")#grey scale value
plt.plot(x,np.sin(x+3),":r")#xcode
plt.show()'''

'''plt.plot(x,np.sin(x),"-g")
plt.xlim(-10,23)
plt.ylim(-40,10)
plt.show()'''

'''plt.plot(x,np.sin(x),"-g")
plt.xlim(-10,23)
plt.ylim(-40,10)
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.title("from scratch")
plt.show()'''



plt.plot(x,np.sin(x),"-g",label="sin X")
plt.plot(x,np.sin(x+1),"--c",label="sin(x+1")
plt.legend()
plt.show()
