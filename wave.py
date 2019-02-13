import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavefile as wav
fs,data=wav.read('music.wav')
print(data,fs)
plt.plot(data)
plt.show()