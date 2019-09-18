from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def line_dir_pt(m,A):
  len = 10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(-20,20,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#len = 10
xx, yy = np.meshgrid([-20,20], [-20,20])


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
k = -1
# change Values here


n1 = np.array([1,k,-1])
n2 = np.array([k,-1,-1])


l = np.cross(n1,n2)
O = np.array([0,0,0])
T  = line_dir_pt(l,O)
print(T)

n1 = np.array([1,k,-1]).reshape((3,1))
c1 = 0
n2 = np.array([k,-1,-1]).reshape((3,1))
c2 = 0
n3 = np.array([1,1,-k]).reshape((3,1))
c3 = 0



z1 = ((c1-n1[0]*xx-n1[1]*yy)*1.0)/(n1[2])
z2 = ((c1-n2[0]*xx-n2[1]*yy)*1.0)/(n2[2])

ax.plot_surface(xx, yy, z1, color='b',alpha=0.1)
ax.plot_surface(xx, yy, z2, color='r',alpha=0.6) 


xx, z3 = np.meshgrid([-20,20], [-20,20])
yy = ((c1-n3[0]*xx-n3[2]*z3)*1.0)/(n3[1])



ax.plot_surface(xx, yy, z3, color='y',alpha=1)
plt.plot(T[0,:],T[1,:],T[2,:],label="Line ")

ax.set_xlabel('$X$-axis')
ax.set_ylabel('$Y$-axis')
ax.set_zlabel('$Z$-axis')
plt.legend(loc = 'best')
#plt.axis('equal')
plt.grid()
plt.show()
