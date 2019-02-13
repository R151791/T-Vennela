import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,100,1)
y=np.sin(np.pi/2-x)
print(y)
plt.stem(x,y)
plt.show()
