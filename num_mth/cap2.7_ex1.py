
#######################################################
### Programa utilizado para aproximar numericamente ###
### a seguinte ODE:                                 ###
###                                                 ###
###     dy/dt = 3 + e^(-t) - 1/2*y, y(0) = 1        ### 
###                                                 ###
### Utilizado o Metodo de Euler:                    ###
### y[n+1] = y[n] +f(t[n], y[n])*(t[n+1] - t[n])    ###
### ----------------------------------------------- ###
### "Equacoes Diferenciais Elementares e Problemas  ###
###   de Valores de Contorno" - Boyce & Diprima     ###   
###   8º Ed. Cap: 2.7, Exemplo: 1                   ###
### ----------------------------------------------- ###
#######################################################

import seaborn as sns
import numpy as np

sns.set(style="darkgrid")

f0 = 1 # Initial condition
dt  = 0.1 # Time interval (0.5, 2) --- 

tn = 5 # Size of grid

N_t =  int(tn/dt) # N_t = tn/dt -- Number of meshgrid points

from numpy import linspace, zeros, exp
t = linspace(0, (N_t)*dt, N_t+1)
y = zeros(N_t+1)
f = zeros(N_t+1)

y[0] = f0
tz = 0
for n in range(N_t):
    f[n] = 3 + np.exp(-t[n]) - (1/2)*y[n]
    #print(f[n])
    y[n+1] = y[n] + dt*f[n]

#########################
### Solucao analitica ###
#########################

ya = 6 - 2*np.exp(-t) - 3*np.exp(-t/2)

################################################################
### Erro entre solução exata analitica (ya) e aproximada (y) ### 
################################################################

e = (y-ya)

############
### Plot ###
############

import matplotlib.pyplot as plt


#plt.scatter(t, y, c='r', s=7, label = 'Numerical', zorder = 100)
plt.plot(t, ya, linewidth=6, color='lightcoral', label='Exact', zorder=1e3)


### Legend ###
legend_properties = {'weight':'semibold',
'size':10}

leg = plt.legend(loc='upper left', prop=legend_properties)
frame = leg.get_frame()
frame.set_color('lightgray')


plt.xlabel('t', size = 12, weight = 'semibold'); 
plt.xticks(size = 10, weight = 'semibold')

plt.ylabel(u'$\phi (t)$', size = 14, weight = 'semibold')
plt.yticks(size = 10, weight = 'semibold')


########################################
### CAMPO DE DIREÇÕES DA EDO:        ###
### dy/dt = -(y/2) + (1/2)*(e^(t/3)) ###
########################################


# Y is dependent variable and X in independent

nx, ny = .1, .1
x = np.arange(0, 6, nx)
y = np.arange(0, 6, ny)
X, Y = np.meshgrid(x, y)
dy = 3 + np.exp(-X) - (1/2)*Y
dx = np.ones(dy.shape)

color = dy
lw = 1
plt.streamplot(X,Y,dx, dy, color=color, density=2., cmap='copper', arrowsize=1)

plt.show()
plt.ion()