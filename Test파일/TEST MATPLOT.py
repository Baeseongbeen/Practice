from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1, 10)
y1 = x *5
y2 = x *1
y3 = x * 0.3
y4 = x * 0.2

plt.plot(x,y1, color='red', linewidth='5', linestyle='dotted')
plt.show()
# plt.subplot(2,2,1)
# plt.plot(x,y1)
# plt.subplot(2,2,2)
# plt.plot(x,y2)
# plt.subplot(2,2,3)
# plt.plot(x,y3)
# plt.subplot(2,2,4)
# plt.plot(x,y4)
# plt.show()