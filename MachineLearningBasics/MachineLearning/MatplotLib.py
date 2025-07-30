#one of the important lib for creations and visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
#stright line plot
#plt.plot([1,2,4,5])
#print(plt.show())

#both axix
#plt.plot([1,3,4,5],[3,4,55,6])
#plt.show()

#for color
#plt.plot([1,2,4,5],color="red")
#print(plt.show())

#sine wave
import numpy as np
x=np.linspace(0,10,100)
#plt.plot(x,np.sin(x))
#plt.show()

#multiple line plot in a single figure
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()