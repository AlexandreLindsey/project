"""FILE_DESCRIPTION

Credits
-------
Created on Fri Mar 8 10:53:03 2024

@author: Odding Luca s2303933, Raffaele Moreci S2304531
@credits: Lindsey Alexandre S2302371
"""

# %% [0] Imports
# Standard library imports.
import math

# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# Local module imports
import constants as c
from odefunction import odefunction


# %% [1] Main Code
def calculConcentrationsIVP(Z, C0):
    sol = solve_ivp(odefunction, Z, C0)
    return [sol.t, sol.y]


def calculConcentrationsEuler(Z, C0):
    Z = np.array(Z)
    C0 = np.array(C0)
    h = 0.00145
    n = math.ceil((Z[1] - Z[0])/h)
    C = np.zeros((C0.shape[0], n))
    xappr = C0
    abscisse = np.arange(Z[0], Z[1], h)

    for i in range(n):
        zi = abscisse[i]
        f = odefunction(zi, xappr)
        for j, element in enumerate(C):
            element[i] = xappr[j]
        xappr = xappr + h*f

    return [abscisse, C]


# %% [2] Testing Code
if __name__ == '__main__':
    C0 = [0.927, 0.278, 1e-5, 1e-1, 1e-1, 1e-1, c.TW(), c.P('tot', 0)]
    t, x = calculConcentrationsEuler([0, c.dim('l')], C0)

    plt.figure()
    plt.plot(t, x[0], label='CH4', linewidth=1)
    plt.plot(t, x[1], label='H2O', linewidth=1)
    plt.plot(t, x[2], label='H2', linewidth=1)
    plt.plot(t, x[3], label='CO', linewidth=1)
    plt.plot(t, x[4], label='CO2', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Concentration')
    plt.xlabel('z')

    plt.figure()
    plt.plot(t, x[5], label='X', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Conversion fractionnaire')
    plt.xlabel('z')

    plt.figure()
    plt.plot(t, x[6], label='T', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Temperature')
    plt.xlabel('z')

    plt.figure()
    plt.plot(t, x[7], label='P', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Pression')
    plt.xlabel('z')

    sol = calculConcentrationsIVP([0, c.dim('l')], C0)

    plt.figure()
    plt.plot(sol[0], sol[1][0], label='CH4', linewidth=1)
    plt.plot(sol[0], sol[1][1], label='H2O', linewidth=1)
    plt.plot(sol[0], sol[1][2], label='H2', linewidth=1)
    plt.plot(sol[0], sol[1][3], label='CO', linewidth=1)
    plt.plot(sol[0], sol[1][4], label='CO2', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Concentration')
    plt.xlabel('z')

    plt.figure()
    plt.plot(sol[0], sol[1][5], label='X', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Conversion fractionnaire')
    plt.xlabel('z')

    plt.figure()
    plt.plot(sol[0], sol[1][6], label='T', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Temperature')
    plt.xlabel('z')

    plt.figure()
    plt.plot(sol[0], sol[1][7], label='P', linewidth=1)
    plt.legend(loc='best')
    plt.ylabel('Pression')
    plt.xlabel('z')
