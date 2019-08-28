from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
def normal_vector(v):
	omat = np.array([[0,1],[-1,0]])
	return np.matmul(omat,v)

def plot_point(A,s):
	plt.plot(A[0],A[1],'o')
	plt.annotate(s,xy=(A[0],A[1]))

def plot_line_segment(A,B,s):
	plt.plot([A[0],B[0]],[A[1],B[1]],label=s)

def plot_line(eqn,labelstr):
	if eqn[1]!=0:
		#plotting line (eqn[0])x + (eqn[1])y = eqn[2]
		slope = -1*eqn[0]/eqn[1]
		intercept = eqn[2]/eqn[1]
		x_vals = np.array([-10,10])
		y_vals = intercept + slope * x_vals
		plt.plot(x_vals, y_vals, label=labelstr)
	else:
		#plotting vertical line (eqn[0])x = eqn[2]
		plt.axvline(eqn[2]/eqn[0],label=labelstr)

def reflection(point, line):
	P=point.reshape((2,1))
	L=line
	#finding normal vector
	n = L[:2]
	#finding parallel vector
	m = normal_vector(n.reshape((2,1)))
	#finding constant
	c=L[-1]
	#converting to column vectors
	n=n.reshape((2,1))
	m=m.reshape((2,1))
	#finding reflection
	R = 2*(((m@m.T-n@n.T)/(m.T@m+n.T@n))@P+c*n)
	return R

def plot_circle(axis,centre,radius,labelstr):
	ax=axis
	c=centre
	r=radius
	ax.add_patch(plt.Circle(c,r,alpha=1,fill=False,label=labelstr))

def plot_parabola(coeff,labelstr):
    #plots the parabola y = a*x**2 + b*x + c
    a,b,c = coeff[0],coeff[1],coeff[2]
    x = np.linspace(-5,5,1000)
    y = a*x**2 + b*x + c
    plt.plot(x,y,label=labelstr)
    

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
plt.axis('equal')
plt.grid()
plt.show()
