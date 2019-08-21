import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def line_gen(A,m):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-4,3,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

omat = np.array([[0,1],[-1,0]])



#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

len = 50
#Standard parabola

y2 = np.linspace(-20,20,len)
y1 = np.power(y2,2)/8

y = np.vstack((y1,y2))

#Given parabola parameters
V = np.array(([0,0],[0,1]))
u = -np.array([4,0])
F = 0

#Affine transformation


#plotting the parabola
plt.plot(y[0,:],y[1,:],label='Parabola')

#c = np.array(c.T)[0]


P = np.array([6,4*np.sqrt(3)]) 
m1 = np.array([-4*np.sqrt(3),4])
O = np.array([0,0])


x_P = line_gen(P,m1)
plt.plot(x_P[0,:],x_P[1,:],label='Normal1')
plt.text(P[0] * (1 - 0.1), P[1] * (1 + 0.1) , 'P1')
plt.plot(P[0], P[1], 'o')

Q = np.array([6,-4*np.sqrt(3)]) 
m2 = np.array([4*np.sqrt(3),4])



x_Q = line_gen(Q,m2)
plt.plot(x_Q[0,:],x_Q[1,:],label='Normal2')
plt.text(Q[0] * (1 - 0.1), Q[1] * (1 - 0.1) , 'P2')
plt.plot(Q[0], Q[1], 'o')


ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()
