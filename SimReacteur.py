"""FILE_DESCRIPTION

Credits
-------
Created on Fri Mar 8 10:53:03 2024

@author: Odding Luca s2303933, Raffaele Moreci S2304531
@credits: Lindsey Alexandre S2302371
"""

# %% [0] Imports
# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp

# Local module imports
from odefunction import odefunction


# %% [1] Main Code
def calculConcentrationsIVP(fun, x_int, y0, mode=0):
    sol = solve_ivp(lambda x, y: fun(x, y, mode), x_int, y0, rtol=0.5e-6,
                    max_step=10e-7)
    return [sol.t, sol.y]


def calculConcentrationsEuler(x_int, y0, step=10e-8):
    if type(y0) is int:
        y0 = np.array([y0])
    else:
        y0 = np.array(y0)
    x = np.arange(x_int[0], x_int[1], step)
    n = x.size
    y = np.zeros((y0.shape[0], n))
    yappr = y0
    for i in range(n):
        f = odefunction(x[i], yappr)
        y.T[i] = yappr
        yappr = yappr + step*f
    return [x, y]
