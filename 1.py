from matplotlib import pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
fs,data=wav.read('myvoice2.wav')
print(2*fs,len(data))
wav.write('lowvoice.wav',0.5*fs,data)
t=np.arange(0,len(data)/fs1,1.0/fs1)
plt.plot(t,data1)
plt.show()


