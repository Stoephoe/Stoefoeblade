import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd
'''
b = 0.25
c = 5.0


y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)

print(y0)
print(t)

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

sol = odeint(pend, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
'''

rho=1.25
v=20
cT_loc=0.1

def dTdr(r,T):
    eq= cT_loc*(np.pi*rho*v**2*r)
    return eq
    
T0=0

r=np.linspace(0,1,100)
sol_1=odeint(dTdr,y0=T0,t=r,tfirst=True)
sol_2=solve_ivp(dTdr,t_span=(0,max(r)),y0=[T0],t_eval=r)

T_sol_m1=sol_1.T[0]

plt.plot(r,T_sol_m1)
plt.xlabel('$r [meters]$', fontsize=22)
plt.ylabel('$T [thrust]$', fontsize=22)
plt.show()