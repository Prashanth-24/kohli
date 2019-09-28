import numpy as np
import matplotlib.pyplot as plt

def inter_circle(Q,r,P1,V):
	a = V.dot(V)
	b = 2 * V.dot(P1 - Q)
	c = P1.dot(P1) + Q.dot(Q) - 2 * P1.dot(Q) - r**2
	disc = b**2 - 4 * a * c
	
	if disc < 0:
		return False, None
		
	sqrt_disc = np.sqrt(disc)
	t1 = (-b + sqrt_disc) / (2 * a)
	t2 = (-b - sqrt_disc) / (2 * a)

	if not (0 <= t1 <= 1 or 0 <= t2 <= 1):
		return False, None
		
	return P1 + t1*V, P1 + t2 * V

Q = np.array([3,-2])   # Centre of circle
r = 5                  # Radius of circle
P1 = np.array([0,1])   # Start of line segment
R_x = -3/5             # abscissa of midpoint of P and Q

V = np.zeros((2,2))

V[:,0] = [1,1]
V[:,1] = np.roots([1,-5,6])
q,p = inter_circle(Q,r,P1,V[1,:])
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + Q).T

plt.plot(x_circ[0,:], x_circ[1,:], label='$\Omega$')
plt.plot([p[0],q[0]], [p[1],q[1]],label='$\Gamma_1$')
plt.plot(p[0], p[1], 'o')
plt.plot(q[0], q[1], 'o')
plt.text((p[0]+0.1)*(1+0.1), p[1]*(1-0.2), 'P')
plt.text((q[0]+0.1)*(1+0.1), q[1]*(1-0.2), 'Q')

q,p = inter_circle(Q,r,P1,V[0,:])
plt.plot([p[0],q[0]], [p[1],q[1]],label='$\Gamma_2$')
plt.plot(p[0], p[1], 'o')
plt.plot(q[0], q[1], 'o')
plt.text((p[0]+0.1)*(1+0.1), p[1]*(1-0.2), 'P\'')
plt.text((q[0]+0.1)*(1+0.1), q[1]*(1-0.2), 'Q\'')

plt.plot(P1[0], P1[1], 'o')
plt.text((P1[0]+0.1)*(1+0.1), P1[1]*(1-0.2), 'C')

plt.grid()
plt.axis('equal')
plt.legend()
plt.show()
