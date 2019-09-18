from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('x.dat')
y = np.loadtxt('y.dat')
x2 = np.loadtxt('x2.dat')
y2 = np.loadtxt('y2.dat')
z = np.loadtxt('z.dat')
z1 = np.loadtxt('z1.dat')
z2 = np.loadtxt('z2.dat')

T = np.loadtxt('T.dat')


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(x, y, z, color='b',alpha=.8)
ax.plot_surface(x, y, z1, color='g',alpha=.8)
ax.plot_surface(x2, z2, y2, color='r',alpha=.8)

plt.plot(T[0,:],T[1,:],T[2,:],label="Line ")



plt.grid()
plt.legend()
plt.show()
