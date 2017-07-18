import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9]
y = [1,3,2,5,7,8,8,9,10,12]
m_x = np.mean(x)
m_y = np.mean(y)
print("Mean of x :", m_x)
print("Mean of y :", m_y)
slope = np.sum((x-m_x)*(y-m_y))/np.sum((x-m_x)*(x-m_x))
print("Slope(b1):", slope)
b0 = m_y - (slope*m_x)
print("b0 coefficient :", b0)
values = [slope*i + b0 for i in x]

print(values)

plt.plot(x,values)

plt.plot(x, y)
plt.show()