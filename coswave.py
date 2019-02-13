import matplotlib.pyplot as plt
import numpy as np
f=9
fs=100
sample=100
x=np.arange(sample)
y=np.cos(2*np.pi*f*x/fs)
plt.plot(x,y)
plt.show()