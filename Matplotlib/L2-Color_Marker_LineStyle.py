import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8]

plt.plot(x, np.power(x,2), 'r.-', x,np.power(x,3),'b+:')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Color, Marker, Line Style")
plt.show()