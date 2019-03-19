import numpy  as np
import matplotlib.pyplot as plt

def Coseno(t,A,B):
	return A*np.sin(t)+B

A = 1

B = 5
x = np.arange(0,10,1)

Imagen = Coseno(x,A,B)

plt.plot(x,Imagen)


#plt.style.use('ggplot')
#fig = plt.figure(figsize=(6, 5))
#ax1 = fig.add_subplot(111)
#ax1.plot(x,Imagen)

plt.show()