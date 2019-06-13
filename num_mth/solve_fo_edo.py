import numpy as np


def ode_fo(f, x0, T, dt):
    N_t = int(round(T/dt)) # Number of meshgrid points

    t = np.linspace(0, (N_t)*dt, N_t+1)
    y = np.zeros(N_t+1)
    f_N = np.zeros(N_t+1)

    y[0] = f0 # Initial condition

    for n in range(N_t):
        f_N[n] = f(t[n],y[n])
        #print(f[n])
        y[n+1] = y[n] + dt*f_N[n]

    return y, t

f = (lambda t, y: 3 + np.exp(-t) - (1/2)*y)
f0 = 1 
dt  = 0.1  
tn = 5

y,t = ode_fo(f, f0, tn, dt)