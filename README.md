import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-4,3,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

omat = np.array([[0,1],[-1,0]])

def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

len = 50
#Standard parabola

y2 = np.linspace(-10,10,len)
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


P = np.array([(5*np.sqrt(3))/4,0]) 
Q = np.array([0,-5/4])

x_P = line_gen(P,Q)
plt.plot(x_P[0,:],x_P[1,:],label='Normal')
plt.text(P[0] * (1 - 0.1), P[1] * (1 + 0.1) , 'P')
plt.plot(P[0], P[1], 'o')

plt.text(Q[0] * (1 - 0.1), Q[1] * (1 + 0.1) , 'Q')
plt.plot(Q[0], Q[1], 'o')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()
